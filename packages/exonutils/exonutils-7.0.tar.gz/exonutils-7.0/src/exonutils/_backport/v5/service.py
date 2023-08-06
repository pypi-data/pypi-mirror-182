# -*- coding: utf-8 -*-
import threading
import logging
from traceback import format_exc

from .daemon import BaseDaemon

__all__ = []


class BaseService(BaseDaemon):

    # interval in sec to check for tasks
    task_check_interval = 5

    # delay in sec to wait for tasks threads exit
    task_exit_delay = 5

    def __init__(self, name=None, logger=None, debug=0):
        super(BaseService, self).__init__(
            name=name, logger=logger, debug=debug)

        # service tasks list
        self.tasks = []

        # suspended tasks list
        self._suspended = []

        # runtime threads buffer
        self._threads = dict()

    def initialize(self):
        self.log.info("Initializing")

        # check service tasks list
        if not self.tasks:
            raise RuntimeError("No tasks loaded !!!")
        for T in self.tasks:
            if not issubclass(T, BaseServiceTask):
                raise RuntimeError("Invalid task: %s" % str(T))
        # debug tasks
        if self.debug >= 2:
            self.log.debug(
                "Loaded tasks: (%s)"
                % ','.join([T.__name__ for T in self.tasks]))

    def execute(self):
        self.check_tasks()

        # checking threads interval
        self.sleep(self.task_check_interval)

    def terminate(self):
        self.log.debug("wait all tasks exit")
        for name in list(self._threads.keys()):
            if self._threads[name].is_alive():
                self._threads[name].join(self.task_exit_delay)

    def stop(self):
        self.term_event.set()

        self.log.info("stopping all tasks")
        for name in list(self._threads.keys()):
            self._threads[name].stop()

    def get_task(self, name):
        for T in self.tasks:
            if name == T.__name__:
                return T
        return None

    def start_task(self, name):
        t_cls = self.get_task(name)
        if not t_cls:
            self.log.warning("invalid task name: %s" % name)
            return False

        if name in self._suspended:
            self._suspended.remove(name)

        if name not in self._threads.keys():
            self.log.info("starting <TASK:%s>" % name)
            t = t_cls(self)
            t.setDaemon(True)
            t.start()
            self._threads[name] = t

        return True

    def stop_task(self, name, suspend=False):
        t_cls = self.get_task(name)
        if not t_cls:
            self.log.warning("invalid task name: %s" % name)
            return False

        if suspend and name not in self._suspended:
            self._suspended.append(name)

        if name in self._threads.keys():
            self.log.info("stopping <TASK:%s>" % name)
            self._threads[name].stop()
            del(self._threads[name])

        return True

    def restart_task(self, name):
        if not self.stop_task(name):
            return False
        return self.start_task(name)

    def check_tasks(self):
        for T in self.tasks:
            try:
                # check and clean dead tasks threads
                t = self._threads.get(T.__name__, None)
                if t and not t.is_alive():
                    del(self._threads[T.__name__])
                    self.log.warning("found dead <TASK:%s>" % T.__name__)

                # stop suspended task
                if T.__name__ in self._threads and \
                        T.__name__ in self._suspended:
                    self.stop_task(T.__name__)

                # start new task
                if T.__name__ not in self._threads and \
                        T.__name__ not in self._suspended:
                    self.start_task(T.__name__)

            except Exception:
                self.log.error(format_exc().strip())


class BaseServiceTask(threading.Thread):

    def __init__(self, service):
        super(BaseServiceTask, self).__init__(
            name=self.__class__.__name__)

        # service instance
        self.service = service

        # task terminate event
        self.term_event = threading.Event()

        # task logger
        self.log = logging.getLogger(self.name)
        self.log.parent = self.service.log
        # debug level
        self.debug = self.service.debug

    def initialize(self):
        pass

    def execute(self):
        raise NotImplementedError()

    def terminate(self):
        pass

    def run(self):
        try:
            # initialize task
            self.initialize()
            # run task forever
            while not self.term_event.is_set():
                self.execute()
        except Exception:
            self.log.error(format_exc().strip())
        except (KeyboardInterrupt, SystemExit):
            pass

        try:
            # terminate task
            self.terminate()
        except Exception:
            self.log.error(format_exc().strip())
        except (KeyboardInterrupt, SystemExit):
            pass

        self.log.info("terminated")

    def start(self):
        super(BaseServiceTask, self).start()

    def stop(self):
        self.term_event.set()

    def sleep(self, timeout):
        if self.term_event.wait(timeout=timeout):
            raise SystemExit()

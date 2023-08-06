#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import queue
from dataclasses import dataclass
from loguru import logger  # noqa


@dataclass
class Job:
    """
    :param func - function to execute.

    :param args - arguments to pass to func.

    :param kwargs - keyword arguments to pass to func.

    :param callback - callback function to execute after func.

    :param block - block next job until the current job is done.
    """
    func: callable = None
    args: tuple = None
    kwargs: dict = None
    callback: callable = None
    block: bool = False


class Executor:
    def __init__(self, number_threads=10, max_queue_size=0):
        """
        :param number_threads: number of threads to run concurrently.

        :param max_queue_size: If maxsize is <= 0, the queue size is infinite.
        """
        self.number_threads = number_threads
        self.max_queue_size = max_queue_size
        self.queue = queue.Queue(maxsize=max_queue_size)
        self.thread_start()

    def send(self, job: Job) -> None:
        """
        Push a job to the queue

        if the queue is full, 'queue.put' will be block until there is a free space in the queue.

        :param job
        """
        if not job.func:
            raise Exception("executor required")
        self.queue.put(job)
        if job.block:
            self.queue.join()

    def thread_start(self) -> None:
        for i in range(self.number_threads):
            threading.Thread(target=self.worker, daemon=True).start()

    def worker(self) -> None:
        while True:
            try:
                job = self.queue.get(timeout=None)
                result = job.func(*job.args, **job.kwargs)
                if job.callback:
                    job.callback(result)
                self.queue.task_done()
            except Exception as e:
                raise Exception(e)

    def wait(self) -> None:
        """
        wait for all jobs to be completed without blocking each other
        :return:
        """
        self.queue.join()

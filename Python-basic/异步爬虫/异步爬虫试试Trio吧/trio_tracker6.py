#!/usr/bin/env python  
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/4 1:55 

import trio


class Tracer(trio.abc.Instrument):
    def before_run(self):
        print("!!! run started")

    def _print_with_task(self, msg, task):
        print(f"{msg}: {task.name}")

    def task_spawned(self, task):
        self._print_with_task("###task scheduled", task)

    def before_task_step(self, task):
        self._print_with_task(">>>about to run one step of task", task)

    def after_task_step(self, task):
        self._print_with_task("<<< task step finished", task)

    def before_io_wait(self, timeout):
        if timeout:
            print(f"### waiting for I/O for up to {timeout} seconds")

        else:
            print("### doing a quick check for I/O")

    def after_io_wait(self, timeout):
        duration = trio.current_time() - self._sleep_time
        print("### finished I/O check (took {} seconds)".format(duration))

    def after_run(self):
        print("!!! run finished")
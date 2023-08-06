#
# rbfly - a library for RabbitMQ Streams using Python asyncio
#
# Copyright (C) 2021-2022 by Artur Wroblewski <wrobell@riseup.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Implementation of queue of messages received from a RabbitMQ stream.
"""

import asyncio
from collections import deque

from libc.stdint cimport int32_t, uint16_t

from ..amqp import MessageCtx

cdef class MessageQueue:
    """
    RabbitMQ stream message queue.

    The queue allows to coordinate receiving of messages from a RabbitMQ
    stream, and enables control of RabbitMQ stream subscription credit.
    """
    cdef:
        int32_t _credit
        uint16_t _queue_threshold
        object _loop
        object _task

        public uint16_t default_credit
        public object data

    def __cinit__(self, default_credit: int, queue_threshold: int):
        """
        Initialize message queue.

        :param default_credit: Default value of RabbitMQ stream
            subscription credit.
        :param queue_threshold: Size of queue determining if RabbitMQ
            stream subscription credit can be renewed.
        """
        self._credit = self.default_credit = default_credit
        self._queue_threshold = queue_threshold

        self.data = deque([]) 

        self._loop = asyncio.get_event_loop()
        self._task = self._loop.create_future()

    cpdef put(self, message: MessageCtx):
        """
        Add message into the queue.
        """
        self.data.append(message)

    def set(self) -> bool:
        """
        Mark queue as populated with messages from RabbitMQ stream.

        Any coroutine waiting with :py:meth:`MessageQueue.wait` is woken
        up.

        Return true if RabbitMQ stream subscription credit needs to be
        renewed.
        """
        cdef uint16_t queue_len
        assert self._credit > 0
        self._credit -= 1
        if not self._task.done():
            self._task.set_result(None)

        return self._credit == 0 and len(self.data) < self._queue_threshold

    async def wait(self) -> None:
        """
        Wait for the queue to be populated with messages from RabbitMQ
        stream.
        """
        task = self._task
        if task.done() and self.data:
            return
        elif task.done():
            task = self._task = self._loop.create_future()
        await task

    @property
    def needs_credit(self) -> bool:
        """
        Check if subscription credit needs to be renewed.
        """
        assert self._credit >= 0
        return self._credit == 0 and len(self.data) == 0

    def reset_credit(self) -> None:
        """
        Reset subscription credit value.

        Note, that it only changes `_credit` attribute, and subscription
        credit needs to be renewed via RabbitMQ Streams protocol as well.

        .. seealso:: :py:meth:`rbfly.streams.protocol.RabbitMQStreamsProtocol`
        """
        self._credit = self.default_credit

    @property
    def task(self):
        return self._task


# vim: sw=4:et:ai

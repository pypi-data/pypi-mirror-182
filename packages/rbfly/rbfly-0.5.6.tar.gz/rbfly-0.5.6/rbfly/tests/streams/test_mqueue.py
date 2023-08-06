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
Unit tests for RabbitMQ stream message queue.
"""

import asyncio

from rbfly.amqp import MessageCtx
from rbfly.streams._mqueue import MessageQueue

import pytest

def test_mqueue_add_msg() -> None:
    """
    Test adding messages to RabbitMQ stream message queue.
    """
    queue = MessageQueue(2, 16)
    queue.put(MessageCtx(1))
    queue.put(MessageCtx(2))

    assert [m.body for m in queue.data] == [1, 2]

@pytest.mark.timeout(1)
@pytest.mark.asyncio
async def test_mqueue_wait() -> None:
    """
    Test waiting for new messages in RabbitMQ stream message queue.
    """
    loop = asyncio.get_event_loop()
    queue = MessageQueue(2, 16)
    queue.put(MessageCtx(1))
    queue.put(MessageCtx(2))

    # queue.set will unblock waiting for the messages
    loop.call_later(0.2, queue.set)
    await queue.wait()

    # there is data in the queue, it will return immediately
    await queue.wait()

def test_mqueue_needs_credit() -> None:
    """
    Test checking if RabbitMQ stream subscription needs credit renewal.
    """
    # initialize the queue with credit 2
    queue = MessageQueue(2, 16)
    queue.put(MessageCtx(1))
    queue.put(MessageCtx(2))
    
    assert not queue.set()  # credit == 1
    assert queue.set()      # credit == 0

    # there is data in the queue, no need for credit renewal
    assert not queue.needs_credit
    while queue.data:
        queue.data.popleft()

    # no data in the queue, credit renewal is required
    assert queue.needs_credit

# vim: sw=4:et:ai

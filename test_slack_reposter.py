import datetime
import pytest
import slack_reposter
from slack_reposter import SlackApiClient
import json


def test_calculate_oldest_post_day():
    client = SlackApiClient()
    oldest_post_day = client.calculate_oldest_post_day(30)
    assert oldest_post_day + datetime.timedelta(days=30) == datetime.datetime.now().replace(hour=0, minute=0, second=0,
                                                                                            microsecond=0)


def test_get_old_posts(mocker):
    mocker.patch('requests.get',
                 return_value="{\"ok\":true,\"messages\":[{\"type\":\"message\",\"user\":\"U012AB3CDE\",\"text\":\"I find you punny and would like to smell your nose letter\",\"ts\":\"1512085950.000216\"},{\"type\":\"message\",\"user\":\"U061F7AUR\",\"text\":\"What, you want to smell my shoes better?\",\"ts\":\"1512104434.000490\"}],\"has_more\":true,\"pin_count\":0,\"response_metadata\":{\"next_cursor\":\"bmV4dF90czoxNTEyMDg1ODYxMDAwNTQz\"}}")
    client = SlackApiClient()
    old_posts = client.get_old_posts('test_id', 10, 10)
    jsonized_old_posts = json.loads(old_posts)
    assert jsonized_old_posts["ok"] == True


def test_get_replies():
    pass


def test_request_old_posts():
    pass


def test_delete_messages():
    pass

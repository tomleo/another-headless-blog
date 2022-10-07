import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from post.models import Post


@pytest.mark.django_db
def test_posts_list():
    # arrange
    client = APIClient()

    # act
    resp = client.get(reverse("post-list"), format="json")

    # assert
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_posts_retrieve():
    # arrange
    client = APIClient()
    post = Post.objects.create(
        title="title 1",
        body="test",
        meta="test",
    )

    # act
    resp = client.get(reverse("post-detail", kwargs={"pk": post.id}), format="json")

    # assert
    assert resp.status_code == status.HTTP_200_OK

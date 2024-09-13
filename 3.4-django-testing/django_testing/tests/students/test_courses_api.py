import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    course = course_factory()
    url = reverse('course-detail', args=[course.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == course.id

@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse('course-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 3

@pytest.mark.django_db
def test_filter_courses_by_id(api_client, course_factory):
    course = course_factory()
    course_factory()  # создаем дополнительный курс
    url = reverse('course-list')
    response = api_client.get(url, data={'id': course.id})
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == course.id

@pytest.mark.django_db
def test_filter_courses_by_name(api_client, course_factory):
    course = course_factory(name='Test Course')
    course_factory()  # создаем дополнительный курс
    url = reverse('course-list')
    response = api_client.get(url, data={'name': 'Test Course'})
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Test Course'

@pytest.mark.django_db
def test_create_course(api_client):
    url = reverse('course-list')
    data = {'name': 'New Course', 'description': 'Course description'}
    response = api_client.post(url, data=data)
    assert response.status_code == 201
    assert response.data['name'] == 'New Course'

@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory()
    url = reverse('course-detail', args=[course.id])
    data = {'name': 'Updated Course'}
    response = api_client.put(url, data=data)
    assert response.status_code == 200
    assert response.data['name'] == 'Updated Course'

@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory()
    url = reverse('course-detail', args=[course.id])
    response = api_client.delete(url)
    assert response.status_code == 204

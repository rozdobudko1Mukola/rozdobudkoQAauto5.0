import pytest
from modules.api.clients.github import GitHub



@pytest.mark.api
def test_user_exist(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exist(github_api):
    r = github_api.get_user('mukolarozdobudko')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannnot_be_found(github_api):
    r = github_api.search_repo('test_repo_cannnot_be_found_mukola')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('t')
    assert r['total_count'] != 0



#individual tasks
@pytest.mark.api
def test_smile_emoji_is_exist(github_api):
    r = github_api.emojis_repo()
    assert 'smile' in r

@pytest.mark.api
def test_smile_emoji_has_valid_link(github_api):
    r = github_api.emojis_repo()
    assert r['smile'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f604.png?v8'


@pytest.mark.api
def test_name_autor_commit(github_api):
    r = github_api.list_commits('rozdobudko1Mukola','rozdobudkoQAauto5.0')
    assert r[0]['commit']['author']['name'] == 'rozdobudo mukola'

@pytest.mark.api
def test_name_autor_commit(github_api):
    r = github_api.list_commits('rozdobudko1Mukola','rozdobudkoQAauto5.0')
    assert r[0]['commit']['author']['email'] == 'rozdobudko.nikolay@gmail.com'

from unittest import TestCase
from store import count_store_by_location_with_kakao

class Test(TestCase):
    def test_count_store_by_location_with_kakao(self):
        gu = '강남구'
        dong_list = ['역삼1동', '역삼2동']
        store_name = '자담치킨'

        count, api_status = count_store_by_location_with_kakao(gu, dong_list, store_name)

        print(gu, store_name, '가게 개수 =', count)
        assert api_status
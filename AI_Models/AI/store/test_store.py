import unittest
from unittest import TestCase
import logging
from store import count_store_by_location_with_kakao


class Test(TestCase):
    def test_count_store_by_location_with_kakao(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        gu = '강남구'
        dong_list = ['역삼1동', '역삼2동']
        store_name = '자담치킨'

        count, api_status = count_store_by_location_with_kakao(gu, dong_list, store_name)

        logging.info(f"[실행 결과] {gu} {store_name}, 가게 개수 = {count}")
        assert api_status

    def test_count_store_by_location_with_kakao_for_multi_users(self):
        gu = '강남구'
        dong_list = ['역삼1동', '역삼2동']
        store_name = '자담치킨'


if __name__ == '__main__':
    unittest.main()
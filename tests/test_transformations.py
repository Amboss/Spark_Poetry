import pytest
from pyspark.sql import SparkSession, types

from quinn.extensions import *

import app.sparksession as S
import app.transformation as T


class TestTransformations(object):

    def test_with_greeting(self):
        """
        Test Spark session
        :return:
        """
        source_data = [("jose", 1), ("li", 2)]

        source_df = S.spark.createDataFrame(source_data, ["name", "age"])
        source_df.show()

        actual_df = T.with_greetings(source_df)
        actual_df.show()

        expected_data = [("jose", 1, "hello!"), ("li", 2, "hello!")]

        expected_df = S.spark.createDataFrame(
            expected_data, ["name", "age", "greeting"]
        )

        assert(expected_df.collect() == actual_df.collect())

    def test_with_clean_first_name(self):
        """
        Test quinn.remove_non_word_characters() function
        :return:
        """
        source_df = S.spark.createDataFrame([
            ("jo&&se", "a"), ("##li", "b"), ("!!sam**", "c")
        ], schema="first_name string, letter string")
        source_df.show()

        actual_df = T.with_clean_first_name(source_df)
        actual_df.show()

        expected_df = S.spark.createDataFrame([
            ("jo&&se", "a", "jose"), ("##li", "b", "li"), ("!!sam**", "c", "sam")
        ], schema="first_name string, letter string, clean_first_name string")

        assert(expected_df.collect() == actual_df.collect())

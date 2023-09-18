# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
  st.set_page_config(page_title='Kannan G\'s portfolio' ,layout="wide")

  st.sidebar.caption('Wish to connect?')
  # st.sidebar.write('Mail: ')
  st.sidebar.write('[LinkedIn](https://www.linkedin.com/in/kannan-g-212242111)')

  st.subheader('Summary')
  st.write("Hi, I'm Kannan. Working as Data Architect @ [Ganit](https://www.ganitinc.com/) with 12+ years of experience in helping business to use thier Data as competitive advantage")

  st.divider()
  st.subheader('Skills')
  col1, col2, col3 = st.columns(3)

  with col1:
    st.markdown("###### Python")
    st.markdown("###### SQL")
    st.markdown("###### Spark")
    st.markdown("###### Docker")

  with col2:
    st.markdown("###### Databricks")
    st.markdown("###### Snowflake")

  with col3:
    st.markdown("###### Azure Data Factory")
    st.markdown("###### Azure Synapse")
    st.markdown("###### AWS Glue")

  st.divider()
  st.subheader('Certifications')
  DEALink='##### Databricks Certified: [Data Engineer Associate](https://scq.io/rqVTqa2)'
  GCALink="##### Google Cloud Certified: [Associate Cloud Engineer](https://www.credential.net/55114231-b1b0-4430-b602-ea78deae5c1d?key=b079ea0eb808fde9a09e9da16ed5d60d7db415926aeb1efcc6e3a6cf76a6a63f)"
  AZDBALink="##### Microsoft Certified: [Azure Database Administrator Associate](https://www.credly.com/badges/5a75c0de-a9b4-49e3-9bba-b26671c16ab0)"
  st.markdown(DEALink,unsafe_allow_html=True)
  st.markdown(GCALink,unsafe_allow_html=True)
  st.markdown(AZDBALink,unsafe_allow_html=True)


if __name__ == "__main__":
    run()

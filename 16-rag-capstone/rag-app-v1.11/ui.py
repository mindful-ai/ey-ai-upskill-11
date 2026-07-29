import streamlit as st
import requests

# -------------------------------
# Configuration
# -------------------------------
API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="Medical Information Assistant",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Medical Information Assistant")
st.write("Ask a medical question and view the response from the backend.")

# -------------------------------
# User Input
# -------------------------------
query = st.text_input(
    "Enter your medical question:",
    placeholder="e.g. Explain Type 2 Diabetes symptoms"
)

# -------------------------------
# Submit Button
# -------------------------------
if st.button("Submit", type="primary"):

    if not query.strip():
        st.error("Please enter a question.")
    else:

        with st.spinner("Fetching response..."):

            try:
                response = requests.get(
                    API_URL,
                    params={"q": query},
                    timeout=60
                )

                response.raise_for_status()

                data = response.json()

                # Extract answer field
                answer = data.get("answer", "No response received.")

                # Display nicely formatted response
                st.markdown("## Response")

                st.markdown(
                    f"""
                    <div style="
                        background-color:#e8f5e9;
                        padding:20px;
                        border-radius:12px;
                        border-left:8px solid #4CAF50;
                        color:#000000;
                        font-size:16px;
                        line-height:1.7;
                        margin-top:10px;
                    ">
                    {answer.replace(chr(10), "<br>")}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except requests.exceptions.HTTPError as e:
                st.error(f"HTTP Error: {e}")

            except requests.exceptions.ConnectionError:
                st.error("Unable to connect to the backend server.")

            except requests.exceptions.Timeout:
                st.error("The request timed out.")

            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")

            except ValueError:
                st.error("The backend did not return valid JSON.")

            except Exception as e:
                st.error(f"Unexpected error: {e}")
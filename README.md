# log-analysis-tool
This project aims to improve the developer experience by helping summarize the big raw log files to assist with finding the RCA.

# Problem Statement

This project is a POC that aims to develop a log analysis tool for meeting joins that provides a comprehensive summary of calls. It will aggregate both service and client logs, enabling users to quickly navigate through raw logs to identify and troubleshoot issues efficiently.

---

# Architecture

<img width="812" alt="image" src="https://github.com/user-attachments/assets/5f24b715-e1a1-43ae-bad9-9fed210e3ed3">


---

# Goals

**Goals:**
- Assist users in narrowing down the relevant logs for debugging issues during meetings.
- Provide an intuitive interface to filter and search through large volumes of log data.

**Non-Goals:**
- Identify or diagnose the actual issues with calls; the tool will not provide definitive solutions to the problems identified.

---

# Prerequisites

- Access to Copilot playground: [Copilot Playground](https://m365playground.prod.substrateai.microsoft.net/playgroundv2)
- Access to Prompt chain work flow in Copilot playground

# Code Flow

<img width="1069" alt="image" src="https://github.com/user-attachments/assets/68f35375-c229-412c-9ea1-ca19c0ee2018">


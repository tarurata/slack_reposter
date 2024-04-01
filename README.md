# Slack Reposter

<img width="721" alt="Pasted_Graphic" src="https://github.com/tarurata/slack_reposter/assets/20917097/a862aad9-2b8d-423e-8a16-0c3c34e88528">

## Overview
Due to a policy change in 2022, posts older than 90 days became invisible. The purpose of this project is to automatically repost these messages to circumvent this restriction.

## Details
Currently, this project is set up to use a specific workspace's introduction channel and performs the following tasks on an irregular basis (within every 90 days):

- From the "Introduction" Channel to the "Past Introduction" Channel
- From the "Past Introduction" Channel to the "Past Introduction" Channel
- Including threads.

## Automated Testing
Currently, there are no automated tests, but they are in development.

## Deployment
None specified.

## TODO
* Aim to unify all clients to use WebClient
  * This is because posts retrieved via WebhookClient are being posted using WebClient.

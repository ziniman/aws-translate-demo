# Translate Site

A website that can display English content in different language using [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/what-is.html) as the translation engine.

## Deploying to AWS

To use this website:

- Create an AWS account.
- Create a S3 bucket with [Website Support](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html).
- Create a new [AWS Cognito Identity Pool](https://docs.aws.amazon.com/cognito/latest/developerguide/tutorial-create-identity-pool.html) with access to unauthenticated identities and provide full access to Amazon Translate.
- Edit `js/config.js` and add your Identity Pool ID.
- Edit `content/strings.js` and add your content.
- Copy the files to S3 and access your website.

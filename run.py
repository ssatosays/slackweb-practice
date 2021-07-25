import settings
import slackweb


def main():
    url: str = settings.url
    text: str = "hello, world."
    slack = slackweb.Slack(url=url)
    slack.notify(text=text)


if __name__ == "__main__":
    main()

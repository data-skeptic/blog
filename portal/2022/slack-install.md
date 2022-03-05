## Creating a Slack Bot

- [ ] Visit [https://api.slack.com](https://api.slack.com/) and create an account.

- [ ] Go to [https://api.slack.com/apps](https://api.slack.com/apps) and click "Create New App"

- [ ] When prompted to create an app "From scratch" or "From an app manifest", choose app manifest.

- [ ] Select the workspace you want to install to.

- [ ] In the **YAML** code below, replace **URL GOES HERE** with the URL provided.

- [ ] Paste the **YAML** code found below in the space for the manifest.  **Be sure** to replace the `request_url` with the provided 

 and use the provide the configuration below
https://4nbaxdraua.execute-api.us-east-1.amazonaws.com/api/api/kyle@dataskeptic.com/slack/5c131033-34ed-4127-b319-45a03f7398aa
```
display_information:
  name: Adam
features:
  app_home:
    home_tab_enabled: true
    messages_tab_enabled: false
    messages_tab_read_only_enabled: false
  bot_user:
    display_name: Adam
    always_online: true
oauth_config:
  scopes:
    user:
      - channels:read
      - files:read
      - users:read
    bot:
      - incoming-webhook
      - files:read
      - channels:read
      - groups:read
      - channels:history
      - reactions:read
      - users:read
settings:
  event_subscriptions:
    request_url: **URL GOES HERE**
    bot_events:
      - app_home_opened
      - app_uninstalled
      - file_created
      - file_shared
      - member_joined_channel
      - message.channels
      - reaction_added
      - team_join
      - tokens_revoked
  org_deploy_enabled: false
  socket_mode_enabled: false
  token_rotation_enabled: false
```

- [ ] Advance through the other steps

- [ ] Click "Install to Workspace"


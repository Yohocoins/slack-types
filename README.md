# Slack Types

Type definitions for Slack API using Pydantic models.

## 📦 Installation

### From GitHub (Recommended)

```bash
pip install git+https://github.com/Yohocoins/slack-types.git
```

## 🚀 Quick Start

```python
from slack_types import TeamInfoResponse, UserInfoResponse, ConversationInfoResponse

# Parse team info
team_response = TeamInfoResponse.model_validate(team_data)

# Parse user info
user_response = UserInfoResponse.model_validate(user_data)

# Parse conversation info
conversation_response = ConversationInfoResponse.model_validate(conversation_data)
```

## 📋 Available Types

- **Team**: `TeamInfoResponse`, `Team`, `TeamIcon`
- **User**: `UserInfoResponse`, `User`, `UserProfile`
- **Conversation**: `ConversationInfoResponse`, `Channel`, `DirectMessage`, `DirectMessageWithMembers`

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Adding New Models

1. **Create a new file** in `slack_types/` for your model type
2. **Update `__init__.py`** to export your new types
3. **Open a Pull Request** with:
   - Clear description of what you're adding
   - Link to the relevant Slack API documentation
   - Example of the API response you're modeling

### Fixing or Changing Existing Models

1. **Explain why** the change is needed
2. **Provide evidence** from Slack docs or real scenario

### General Guidelines

- All fields must be required (no optional fields unless Slack API allows null)
- Follow existing naming conventions
- Test your changes with real Slack API responses

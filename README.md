# Azure AI Chat App 🤖

A production-ready generative AI chat application built with **Azure OpenAI**, **Azure AI Foundry**, and **Python**. This project demonstrates enterprise-grade cloud architecture, secure API integration, and modern DevOps practices.

## 📋 Overview

This project showcases:
- ✅ Cloud-based AI model integration (Azure OpenAI)
- ✅ Enterprise authentication (Entra ID/Azure)
- ✅ Conversational AI with context awareness
- ✅ Cost optimization in cloud environments
- ✅ Production-ready error handling and logging
- ✅ Clean code architecture and best practices

**Perfect for**: Technical portfolios, enterprise AI solutions, or AI engineering interviews.

---

## 🎯 Key Features

### Core Capabilities
- **Real-time Chat Interface**: Interactive terminal-based AI chatbot
- **Context-Aware Conversations**: Maintains chat history using Azure response IDs
- **Streaming Responses**: Real-time text display for better UX
- **Model Flexibility**: Easy switching between Azure OpenAI models

### Security & Enterprise Features
- **Azure Entra ID**: Secure authentication via `az login`
- **DefaultAzureCredential**: Enterprise-grade credential management
- **No Hardcoded Secrets**: Environment-based configuration
- **RBAC Ready**: Integrates with Azure role-based access control

### Cost Optimization
- **Efficient Model Usage**: ~$0.01-$0.05 per 1000 test interactions
- **Production Monitoring**: Ready for Azure cost tracking
- **Scalable Design**: Built for enterprise deployments

---

## 🏗 Architecture
- **User Terminal → Python OpenAI SDK → Azure Authentication →
- **Azure OpenAI Endpoint → AI Foundry → GPT-4 Turbo Model

**Key Components:**
1. **Authentication Layer**: Azure Entra ID with `DefaultAzureCredential`
2. **API Layer**: OpenAI SDK communicating with Azure OpenAI
3. **Model Layer**: GPT-4 Turbo for intelligent responses
4. **Context Layer**: Response ID tracking for conversation continuity

---

## 🛠 Tech Stack

**Cloud & AI**
- Azure OpenAI Service
- Azure AI Foundry
- Azure Entra ID

**Languages & Frameworks**
- Python 3.13
- OpenAI Python SDK
- Azure Identity SDK

**DevOps**
- Git/GitHub
- Virtual Environments
- Environment Configuration

---

## 📦 Prerequisites

- Python 3.13+
- Azure subscription with OpenAI resources
- Azure CLI installed
- Git

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/esjimenezp/azure-ai-chat-app.git
cd azure-ai-chat-app
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Azure
Create `.env` file:
AZURE_OPENAI_ENDPOINT=https://your-project.openai.azure.com/
MODEL_DEPLOYMENT=gpt-4-turbo

Get these values from:
- Azure Portal → AI Foundry Project → Home page

### 5. Authenticate
```bash
az login
```

### 6. Run the App
```bash
python chat-app.py
```

---

## 💬 Usage Example
<img width="769" height="614" alt="Screenshot 2026-06-28 at 8 10 06 a m" src="https://github.com/user-attachments/assets/6e1e11e9-ec8b-4cb8-ae25-016923e5c05b" />

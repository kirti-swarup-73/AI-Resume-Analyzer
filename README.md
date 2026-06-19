# AI Resume Analyzer

AI-powered Resume Analyzer that evaluates resumes against job descriptions, calculates ATS compatibility, identifies missing skills, and provides improvement suggestions using Gemini AI.

## Live Demo

https://ai-resume-analyzer-psi-dun.vercel.app

## Features

- Upload PDF Resume
- Extract Resume Content
- Compare Resume with Job Description
- ATS Match Score Generation
- Missing Skills Detection
- Resume Improvement Suggestions
- Analysis History Storage
- Cloud Deployment

## Tech Stack

### Frontend
- React.js
- JavaScript
- HTML5
- CSS3

### Backend
- Python
- Flask

### Database
- MongoDB Atlas

### AI Integration
- Google Gemini API

### Deployment
- Vercel (Frontend)
- Render (Backend)

## Project Architecture

Frontend (React)
↓
Flask API
↓
Gemini API
↓
MongoDB Atlas

## How It Works

1. Upload Resume PDF
2. Enter Job Description
3. Resume text is extracted
4. Gemini AI analyzes resume against the job description
5. ATS score and recommendations are generated
6. Analysis history is stored in MongoDB

## Screenshots

### Home Page
Upload resume and paste job description.

### Analysis Result
Displays ATS score, missing skills, and improvement suggestions.

## Installation

### Clone Repository

```bash
git clone https://github.com/kirti-swarup-73/AI-Resume-Analyzer.git
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

## Environment Variables

Create a .env file:

```env
GEMINI_API_KEY=YOUR_API_KEY
MONGO_URI=YOUR_MONGODB_URI
```

## Future Improvements

- Resume Download Feature
- Multiple Resume Formats
- User Authentication
- Resume Ranking System
- Dashboard Analytics

## Author

Kirti Swarup Mohapatra

Live Demo:
https://ai-resume-analyzer-psi-dun.vercel.app

Repository:
https://github.com/kirti-swarup-73/AI-Resume-Analyzer

GitHub:
https://github.com/kirti-swarup-73

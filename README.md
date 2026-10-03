# 📚 StudyMate

> An AI-powered study companion built for a college friend studying Computer Science and Engineering.

## 🎯 The Problem

My college friend has trouble studying from long lecture notes and preparing for exams.

Long notes can contain a lot of information, but it can be difficult to quickly identify the important concepts, definitions, and possible exam questions.

I built StudyMate to turn those long notes into focused study material.

## 💡 What StudyMate Does

A student can paste their study notes, choose their subject and difficulty level, and ask StudyMate to create:

- 📝 **Exam Summary** — concise revision notes
- 💡 **Simple Explanation** — easier explanations of difficult concepts
- ❓ **Practice Quiz** — multiple-choice and conceptual questions
- 🃏 **Flashcards** — question-and-answer cards for revision

The application currently supports subjects such as:

- Data Structures & Algorithms
- Database Management Systems
- Operating Systems
- Computer Networks
- Object-Oriented Programming
- Software Engineering
- Computer Architecture

## 🤖 Open-Source AI

StudyMate uses the open-weight:

`google/gemma-3-4b-it`

model through Hugging Face's inference router.

The AI model is the core of the application. StudyMate sends the student's notes together with a task-specific prompt and uses the model's response to generate revision material.

## 🌱 Why Open Innovation Matters

I wanted the core intelligence of StudyMate to be based on an open-weight AI model rather than building the project around a proprietary model.

Using an open-weight model gives the project more flexibility around how the AI is used and makes it possible to change or experiment with the underlying model in the future.

For this prototype, inference is performed through Hugging Face because the target laptop has limited hardware and cannot efficiently run a modern language model locally.

This means StudyMate is **not currently an offline application**. Notes are sent to the configured inference service when an AI feature is used.

## 🏗️ How It Works

```text
Student
   │
   ▼
Paste study notes
   │
   ▼
Choose subject + difficulty
   │
   ▼
Select a study feature
   │
   ▼
StudyMate prompt
   │
   ▼
Gemma 3 4B
   │
   ▼
Study material

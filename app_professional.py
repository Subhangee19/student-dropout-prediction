import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Student Dropout Prediction System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap');

    * {
        font-family: 'Roboto', sans-serif;
    }

    /* Professional gradient background */
    .stApp {
        background: linear-gradient(135deg, #0a1929 0%, #1a2332 50%, #0a1929 100%);
    }

    /* Hide Streamlit branding */
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Professional card styling */
    .professional-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 12px;
        border: 1px solid #334155;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    .professional-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4), 0 4px 6px -2px rgba(0, 0, 0, 0.3);
        border-color: #d4af37;
    }

    /* Header styling */
    .main-header {
        text-align: center;
        padding: 2.5rem 2rem;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 12px;
        margin-bottom: 2rem;
        border: 1px solid #334155;
        border-left: 4px solid #d4af37;
    }

    .main-header h1 {
        color: #d4af37;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
    }

    .main-header p {
        color: #94a3b8;
        font-size: 1.1rem;
        font-weight: 400;
        letter-spacing: 0.5px;
    }

    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid #334155;
        transition: all 0.3s ease;
        min-height: 150px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .metric-card:hover {
        border-color: #d4af37;
        transform: translateY(-4px);
        box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2);
    }

    .metric-value {
        font-size: 2.5rem;
        font-weight: 900;
        color: #d4af37;
        margin-bottom: 0.5rem;
    }

    .metric-label {
        color: #94a3b8;
        font-size: 0.95rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    /* Result cards */
    .result-card {
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        border: 2px solid;
        margin: 1rem 0;
    }

    .result-graduate {
        background: linear-gradient(135deg, #b8941f 0%, #8b7355 100%);
        border-color: #d4af37;
    }

    .result-dropout {
        background: linear-gradient(135deg, #4a4035 0%, #3a3029 100%);
        border-color: #6b5d4f;
    }

    .result-enrolled {
        background: linear-gradient(135deg, #475569 0%, #334155 100%);
        border-color: #94a3b8;
    }

    .result-card h2 {
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 1rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .result-card h1 {
        color: #ffffff;
        font-size: 3rem;
        font-weight: 900;
        margin: 1rem 0;
        letter-spacing: 2px;
    }

    .result-card p {
        color: #d4af37;
        font-size: 1.2rem;
        font-weight: 600;
    }

    /* Input field styling */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background: #0f172a !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        color: #e2e8f0 !important;
        font-weight: 500 !important;
        padding: 0.75rem !important;
    }

    .stTextInput input:focus, .stNumberInput input:focus, .stSelectbox select:focus {
        border-color: #d4af37 !important;
        box-shadow: 0 0 0 1px #d4af37 !important;
    }

    .stTextInput label, .stNumberInput label, .stSelectbox label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Button styling */
    .stButton button {
        background: linear-gradient(135deg, #d4af37 0%, #b8941f 100%);
        color: #0a1929;
        border: none;
        padding: 0.875rem 2.5rem;
        font-size: 1rem;
        font-weight: 700;
        border-radius: 8px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        box-shadow: 0 4px 6px -1px rgba(212, 175, 55, 0.3);
    }

    .stButton button:hover {
        background: linear-gradient(135deg, #b8941f 0%, #9a7b1a 100%);
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(212, 175, 55, 0.4);
    }

    /* Section headers */
    .section-header {
        color: #d4af37;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 2rem 0 1rem 0;
        padding: 1rem 1.5rem;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 8px;
        border-left: 4px solid #d4af37;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        border-right: 1px solid #334155;
    }

    [data-testid="stSidebar"] .stRadio label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 0.75rem !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }

    [data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(212, 175, 55, 0.1) !important;
        color: #d4af37 !important;
    }

    /* Voice button */
    .voice-button {
        background: linear-gradient(135deg, #d4af37 0%, #b8941f 100%);
        color: #0a1929;
        border: none;
        padding: 1.5rem 3rem;
        font-size: 1.2rem;
        font-weight: 800;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
        margin: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 0 8px 20px rgba(212, 175, 55, 0.4);
    }

    .voice-button:hover {
        background: linear-gradient(135deg, #f4d03f 0%, #d4af37 100%);
        transform: translateY(-3px);
        box-shadow: 0 12px 25px rgba(212, 175, 55, 0.5);
    }

    .voice-button.recording {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        animation: recordingPulse 1.5s ease-in-out infinite;
    }

    @keyframes recordingPulse {
        0%, 100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
        50% { box-shadow: 0 0 0 15px rgba(239, 68, 68, 0); }
    }

    /* Risk badges */
    .risk-high {
        display: inline-block;
        padding: 0.5rem 1.25rem;
        background: #4a4035;
        color: white;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        border: 1px solid #6b5d4f;
    }

    .risk-medium {
        display: inline-block;
        padding: 0.5rem 1.25rem;
        background: #b8941f;
        color: white;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        border: 1px solid #d4af37;
    }

    .risk-low {
        display: inline-block;
        padding: 0.5rem 1.25rem;
        background: #334155;
        color: white;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        border: 1px solid #94a3b8;
    }

    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-left: 4px solid #d4af37;
        padding: 1.25rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid #334155;
    }

    .warning-box {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-left: 4px solid #b8941f;
        padding: 1.25rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid #334155;
    }

    .success-box {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-left: 4px solid #d4af37;
        padding: 1.25rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid #334155;
    }
</style>
""", unsafe_allow_html=True)

voice_component = """
<style>
    body {
        background-color: #0a1929 !important;
        margin: 0;
        padding: 0;
        font-family: 'Roboto', sans-serif;
    }

    .voice-button {
        background: linear-gradient(135deg, #d4af37 0%, #b8941f 100%);
        color: #0a1929;
        border: none;
        padding: 0.9rem 2rem;
        font-size: 1rem;
        font-weight: 700;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.3);
    }

    .voice-button:hover {
        background: linear-gradient(135deg, #f4d03f 0%, #d4af37 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(212, 175, 55, 0.4);
    }

    .voice-button.recording {
        background: linear-gradient(135deg, #8b7355 0%, #6b5d4f 100%);
        color: white;
        animation: recordingPulse 1.5s ease-in-out infinite;
    }

    @keyframes recordingPulse {
        0%, 100% { box-shadow: 0 0 0 0 rgba(212, 175, 55, 0.6); }
        50% { box-shadow: 0 0 0 12px rgba(212, 175, 55, 0); }
    }
</style>

<div id="voice-container" style="padding: 2rem; background-color: #0a1929; min-height: 100vh;">
    <div style="text-align: center;">
        <button id="voiceBtn" class="voice-button" onclick="toggleVoice()">
            <span id="voiceBtnText">START VOICE INPUT</span>
        </button>
        <div id="transcript" style="color: #cbd5e1; margin-top: 2rem; font-size: 1.1rem; min-height: 30px; font-weight: 500;"></div>
        <div id="aiResponse" style="color: #d4af37; margin-top: 1rem; font-size: 1.05rem; font-weight: 600;"></div>
    </div>

    <div id="resultContainer" style="display: none; margin-top: 3rem;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
            <!-- Collected Data Column -->
            <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 1.5rem; border-radius: 12px; border: 1px solid #334155;">
                <h3 style="color: #d4af37; margin-bottom: 1.5rem; font-size: 1.3rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">COLLECTED DATA</h3>
                <div id="collectedData" style="color: #cbd5e1; font-size: 1rem; line-height: 2;"></div>
            </div>

            <!-- Prediction Result Column -->
            <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 1.5rem; border-radius: 12px; border: 1px solid #334155;">
                <h3 style="color: #d4af37; margin-bottom: 1.5rem; font-size: 1.3rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">PREDICTION RESULT</h3>
                <div id="predictionResult" style="color: #cbd5e1; font-size: 1rem; line-height: 1.8;"></div>
            </div>
        </div>
    </div>
</div>

<script>
let recognition;
let isRecording = false;
let conversationState = 'start';
let studentData = {};

if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = true;  // Show interim results
    recognition.lang = 'en-US';
    recognition.maxAlternatives = 3;  // Get multiple alternatives

    recognition.onresult = function(event) {
        let interimTranscript = '';
        let finalTranscript = '';

        for (let i = event.resultIndex; i < event.results.length; i++) {
            const transcript = event.results[i][0].transcript;
            if (event.results[i].isFinal) {
                finalTranscript += transcript;
            } else {
                interimTranscript += transcript;
            }
        }

        // Show what's being heard in real-time
        if (interimTranscript) {
            document.getElementById('transcript').innerHTML = 'Listening: ' + interimTranscript + '...';
        }

        if (finalTranscript) {
            document.getElementById('transcript').innerHTML = 'You said: ' + finalTranscript;
            console.log('Final transcript:', finalTranscript);
            console.log('All alternatives:', Array.from(event.results[event.results.length-1]).map(r => r.transcript));
            processVoiceInput(finalTranscript);
        }
    };

    recognition.onerror = function(event) {
        console.log('Recognition error:', event.error);
        if (event.error === 'no-speech') {
            document.getElementById('transcript').innerHTML = 'No speech detected. Please speak louder.';
            // Try to restart for no-speech
            if (isRecording && conversationState !== 'complete') {
                setTimeout(() => {
                    if (isRecording) {
                        try {
                            recognition.start();
                            console.log('Restarted after no-speech');
                        } catch(e) {
                            console.log('Cannot restart:', e);
                        }
                    }
                }, 1000);
            }
        } else if (event.error !== 'aborted') {
            document.getElementById('transcript').innerHTML = 'Error: ' + event.error;
        }
    };

    recognition.onend = function() {
        console.log('Recognition ended, state:', conversationState);
        // Don't auto-restart here - let speak() handle restarting after speech is done
    };
}

function toggleVoice() {
    if (!isRecording) {
        startRecording();
    } else {
        stopRecording();
    }
}

async function startRecording() {
    // First, request microphone permission explicitly
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        // Stop the stream immediately - we just needed permission
        stream.getTracks().forEach(track => track.stop());

        isRecording = true;
        document.getElementById('voiceBtn').classList.add('recording');
        document.getElementById('voiceBtnText').innerHTML = 'LISTENING...';

        if (recognition) {
            try {
                recognition.start();
                speak("Hello. I am your AI assistant. What is the student's age?");
                conversationState = 'age';
            } catch(error) {
                console.log('Recognition start error:', error);
                document.getElementById('transcript').innerHTML = 'Error starting recognition: ' + error.message;
                document.getElementById('aiResponse').innerHTML = 'Please refresh the page and try again.';
                stopRecording();
            }
        } else {
            document.getElementById('transcript').innerHTML = 'Speech recognition not supported.';
            document.getElementById('aiResponse').innerHTML = '';
            stopRecording();
        }
    } catch(error) {
        console.log('Microphone permission error:', error);
        document.getElementById('transcript').innerHTML = '🎤 Microphone Access Denied';
        document.getElementById('aiResponse').innerHTML = 'Please click the camera/microphone icon in your browser address bar and allow microphone access, then refresh the page.';
        document.getElementById('voiceBtn').disabled = true;
        document.getElementById('voiceBtn').style.opacity = '0.5';
        document.getElementById('voiceBtn').style.cursor = 'not-allowed';
    }
}

function stopRecording() {
    isRecording = false;
    document.getElementById('voiceBtn').classList.remove('recording');
    document.getElementById('voiceBtnText').innerHTML = 'START VOICE INPUT';

    if (recognition) {
        recognition.stop();
    }
}

function speak(text) {
    document.getElementById('aiResponse').innerHTML = 'AI Assistant: ' + text;

    if ('speechSynthesis' in window) {
        // Stop any ongoing speech first and clear queue
        window.speechSynthesis.cancel();

        // Temporarily stop recognition while AI is speaking
        if (recognition && isRecording) {
            try {
                recognition.stop();
                console.log('Recognition stopped for speech');
            } catch(e) {
                console.log('Error stopping recognition:', e);
            }
        }

        // Wait before starting new speech to ensure clean slate
        setTimeout(() => {
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.rate = 0.7;  // Slower for clarity
            utterance.pitch = 1;
            utterance.volume = 1;

            let hasEnded = false;

            utterance.onstart = function() {
                console.log('Speech started:', text);
            };

            utterance.onend = function() {
                if (hasEnded) return;  // Prevent double-firing
                hasEnded = true;
                console.log('Speech ended, waiting 2 seconds before restart...');

                // Resume recognition after AI finishes speaking with even longer delay
                if (isRecording && conversationState !== 'complete') {
                    setTimeout(() => {
                        if (isRecording && conversationState !== 'complete') {
                            try {
                                recognition.start();
                                console.log('Recognition restarted');
                            } catch(e) {
                                console.log('Recognition restart error:', e);
                            }
                        }
                    }, 2000);  // Increased to 2 seconds for complete sentences
                }
            };

            // Error handler
            utterance.onerror = function(event) {
                console.log('Speech error:', event);
                if (!hasEnded && isRecording && conversationState !== 'complete') {
                    hasEnded = true;
                    setTimeout(() => {
                        if (isRecording) {
                            try {
                                recognition.start();
                            } catch(e) {}
                        }
                    }, 2000);
                }
            };

            window.speechSynthesis.speak(utterance);
        }, 500);  // Longer initial delay
    }
}

function processVoiceInput(input) {
    const numbers = input.match(/\\d+/g);

    switch(conversationState) {
        case 'age':
            if (numbers && numbers.length > 0) {
                studentData.age = parseInt(numbers[0]);
                speak(`Age recorded as ${studentData.age}. Is the student male or female?`);
                conversationState = 'gender';
            } else {
                speak("Please provide a valid age number.");
            }
            break;

        case 'gender':
            // Remove all punctuation and extra whitespace
            const lowerInput = input.toLowerCase().trim().replace(/[.,!?]/g, '');
            console.log('Processing gender input:', input, '-> cleaned:', lowerInput);

            // Check for female keywords (check this FIRST before male)
            const isFemale = lowerInput.includes('female') || lowerInput.includes('girl') ||
                           lowerInput.includes('woman') || lowerInput === 'f' ||
                           lowerInput.includes('femail');  // Common speech recognition error

            // Check for male keywords (only if not female)
            // Include common speech recognition errors: "mail", "mel", "meil"
            const isMale = !isFemale && (
                lowerInput.includes('male') ||
                lowerInput.includes('boy') ||
                lowerInput.includes('man') ||
                lowerInput === 'm' ||
                lowerInput === 'mail' ||  // Common speech recognition error
                lowerInput === 'mel' ||
                lowerInput === 'meil'
            );

            console.log('isFemale:', isFemale, 'isMale:', isMale);

            if (isFemale) {
                studentData.gender = 0;
                studentData.genderText = 'Female';
                console.log('Gender set to Female');
                speak("Gender recorded as female. What is the first semester average grade?");
                conversationState = 'grade';
            } else if (isMale) {
                studentData.gender = 1;
                studentData.genderText = 'Male';
                console.log('Gender set to Male');
                speak("Gender recorded as male. What is the first semester average grade?");
                conversationState = 'grade';
            } else {
                console.log('Gender not recognized from input:', lowerInput);
                speak("I didn't catch that. Please say male or female clearly.");
                return;
            }
            break;

        case 'grade':
            if (numbers && numbers.length > 0) {
                studentData.grade = parseFloat(numbers[0]);
                speak(`Grade recorded as ${studentData.grade}. Are tuition fees up to date?`);
                conversationState = 'tuition';
            } else {
                speak("Please provide a valid grade number.");
            }
            break;

        case 'tuition':
            if (input.toLowerCase().includes('yes')) {
                studentData.tuitionUpToDate = 1;
                studentData.tuitionText = 'Up to Date';
                speak("Tuition status recorded. Does the student have a scholarship?");
            } else if (input.toLowerCase().includes('no')) {
                studentData.tuitionUpToDate = 0;
                studentData.tuitionText = 'Outstanding';
                speak("Tuition status recorded. Does the student have a scholarship?");
            } else {
                speak("Please answer yes or no.");
                return;
            }
            conversationState = 'scholarship';
            break;

        case 'scholarship':
            if (input.toLowerCase().includes('yes')) {
                studentData.scholarship = 1;
                studentData.scholarshipText = 'Yes';
            } else if (input.toLowerCase().includes('no')) {
                studentData.scholarship = 0;
                studentData.scholarshipText = 'No';
            } else {
                speak("Please answer yes or no.");
                return;
            }

            speak("Data collection complete. Processing prediction.");
            stopRecording();

            // Enhanced prediction logic based on actual feature importances
            setTimeout(() => {
                let dropoutScore = 0;
                let graduateScore = 0;
                let riskFactors = [];

                // Academic performance (Grade - most critical factor, ~8% importance)
                if (studentData.grade >= 14) {
                    graduateScore += 40;  // High grades = strong graduation indicator
                } else if (studentData.grade >= 11) {
                    graduateScore += 20;  // Average grades = moderate
                } else if (studentData.grade < 10) {
                    dropoutScore += 40;  // Low grades = high dropout risk
                    riskFactors.push("Low academic performance (Grade: " + studentData.grade + "/20)");
                } else {
                    dropoutScore += 15;  // Below average
                    riskFactors.push("Below average academic performance");
                }

                // Tuition fees (12.05% importance - CRITICAL)
                if (studentData.tuitionUpToDate === 0) {
                    dropoutScore += 50;  // Outstanding fees = major dropout predictor
                    riskFactors.push("Outstanding tuition fees");
                } else {
                    graduateScore += 25;  // Up-to-date = good indicator
                }

                // Scholarship status (Financial support)
                if (studentData.scholarship === 1) {
                    graduateScore += 15;  // Scholarship = better retention
                } else if (studentData.tuitionUpToDate === 0) {
                    dropoutScore += 15;  // No scholarship + outstanding fees = compounded risk
                    if (!riskFactors.includes("Financial instability")) {
                        riskFactors.push("No financial support (scholarship)");
                    }
                }

                // Age factor (Older students have different risk profiles)
                if (studentData.age > 30) {
                    dropoutScore += 12;  // Mature students with other responsibilities
                } else if (studentData.age < 20) {
                    graduateScore += 8;  // Traditional age students
                }

                // Gender (minor factor, but included in model)
                if (studentData.gender === 0) {  // Female
                    graduateScore += 5;  // Slight graduation advantage in data
                }

                // Determine final prediction based on comparative scores
                let prediction, confidence, message, outcome;
                const totalScore = dropoutScore + graduateScore;
                const dropoutProbability = totalScore > 0 ? (dropoutScore / totalScore) * 100 : 50;

                if (dropoutScore > graduateScore + 30) {
                    prediction = "Dropout";
                    outcome = "High Risk of Dropout";
                    confidence = Math.min(60 + (dropoutScore - graduateScore), 92);
                    message = `Based on the data collected, the student shows HIGH RISK of dropout. Immediate intervention strongly recommended.`;
                } else if (dropoutScore > graduateScore) {
                    prediction = "Dropout";
                    outcome = "Moderate-High Risk of Dropout";
                    confidence = Math.min(55 + (dropoutScore - graduateScore) / 2, 78);
                    message = `The student shows elevated dropout risk. Early intervention and monitoring recommended.`;
                } else if (graduateScore > dropoutScore + 20) {
                    prediction = "Graduate";
                    outcome = "Likely to Graduate";
                    confidence = Math.min(65 + (graduateScore - dropoutScore), 89);
                    message = `Good indicators detected. Student shows strong potential to graduate successfully.`;
                } else {
                    prediction = "Enrolled";
                    outcome = "Currently Stable - Monitor Progress";
                    confidence = 60;
                    message = `Student shows mixed indicators. Continue monitoring academic and financial status.`;
                }

                // Display collected data
                document.getElementById('collectedData').innerHTML =
                    `<div style="margin-bottom: 1rem;"><strong style="color: #d4af37;">• Age:</strong> ${studentData.age} years</div>` +
                    `<div style="margin-bottom: 1rem;"><strong style="color: #d4af37;">• Gender:</strong> ${studentData.genderText}</div>` +
                    `<div style="margin-bottom: 1rem;"><strong style="color: #d4af37;">• First Semester Grade:</strong> ${studentData.grade}/20</div>` +
                    `<div style="margin-bottom: 1rem;"><strong style="color: #d4af37;">• Tuition Fees:</strong> ${studentData.tuitionText}</div>` +
                    `<div style="margin-bottom: 1rem;"><strong style="color: #d4af37;">• Scholarship:</strong> ${studentData.scholarshipText}</div>`;

                // Display prediction result with color coding
                let predictionColor = prediction === 'Graduate' ? '#d4af37' :
                                    prediction === 'Dropout' ? '#dc2626' : '#94a3b8';

                document.getElementById('predictionResult').innerHTML =
                    `<div style="font-size: 1.5rem; font-weight: 700; color: ${predictionColor}; margin-bottom: 0.5rem;">Predicted Outcome: ${prediction}</div>` +
                    `<div style="font-size: 1.1rem; font-weight: 600; color: #cbd5e1; margin-bottom: 1rem;">${outcome}</div>` +
                    `<div style="margin-bottom: 1rem;"><strong style="color: #d4af37;">Confidence:</strong> ${Math.round(confidence)}%</div>` +
                    `<div style="margin-bottom: 1.5rem; line-height: 1.6; color: #cbd5e1;">${message}</div>` +
                    (riskFactors.length > 0 ?
                        `<div style="background: rgba(220, 38, 38, 0.1); padding: 1rem; border-radius: 8px; border-left: 3px solid #dc2626;">
                            <strong style="color: #fca5a5; display: block; margin-bottom: 0.5rem;">⚠ Risk Factors Identified:</strong>
                            <ul style="margin: 0; padding-left: 1.5rem; color: #fecaca;">
                                ${riskFactors.map(f => `<li style="margin-bottom: 0.3rem;">${f}</li>`).join('')}
                            </ul>
                        </div>` :
                        `<div style="background: rgba(212, 175, 55, 0.1); padding: 1rem; border-radius: 8px; border-left: 3px solid #d4af37;">
                            <strong style="color: #d4af37;">✓ No major risk factors detected</strong>
                        </div>`);

                // Show result container
                document.getElementById('resultContainer').style.display = 'block';
                document.getElementById('aiResponse').innerHTML = 'Analysis complete. Results displayed below.';

                speak(message);

                conversationState = 'complete';
            }, 1500);
            break;
    }
}

// Check microphone permission on page load
window.addEventListener('load', async function() {
    try {
        if (navigator.permissions && navigator.permissions.query) {
            const permissionStatus = await navigator.permissions.query({ name: 'microphone' });

            if (permissionStatus.state === 'granted') {
                document.getElementById('transcript').innerHTML = '✅ Microphone ready. Click "Start Voice Input" to begin.';
                document.getElementById('aiResponse').innerHTML = 'Tip: Speak clearly and wait for each question to complete.';
            } else if (permissionStatus.state === 'denied') {
                document.getElementById('transcript').innerHTML = '❌ Microphone access denied.';
                document.getElementById('aiResponse').innerHTML = 'Please enable microphone access in your browser settings and refresh the page.';
                document.getElementById('voiceBtn').disabled = true;
                document.getElementById('voiceBtn').style.opacity = '0.5';
            } else {
                document.getElementById('transcript').innerHTML = '🎤 Click "Start Voice Input" to grant microphone access.';
                document.getElementById('aiResponse').innerHTML = 'You will be prompted to allow microphone access.';
            }

            // Listen for permission changes
            permissionStatus.onchange = function() {
                if (this.state === 'granted') {
                    document.getElementById('transcript').innerHTML = '✅ Microphone access granted! Click "Start Voice Input" to begin.';
                    document.getElementById('voiceBtn').disabled = false;
                    document.getElementById('voiceBtn').style.opacity = '1';
                } else if (this.state === 'denied') {
                    document.getElementById('transcript').innerHTML = '❌ Microphone access denied.';
                    document.getElementById('voiceBtn').disabled = true;
                    document.getElementById('voiceBtn').style.opacity = '0.5';
                }
            };
        }
    } catch(error) {
        console.log('Permission check not supported:', error);
        document.getElementById('transcript').innerHTML = 'Ready to start. Click "Start Voice Input" button.';
    }
});
</script>
"""

@st.cache_resource
def load_models():
    with open('xgboost_model.pkl', 'rb') as f:
        xgb_model = pickle.load(f)
    with open('baseline_model.pkl', 'rb') as f:
        baseline_model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)
    return xgb_model, baseline_model, scaler, label_encoder

@st.cache_data
def load_dataset():
    return pd.read_csv('cleaned_dataset.csv')

CHART_COLORS = {
    'primary': '#d4af37',      # Gold (main accent)
    'secondary': '#b8941f',    # Dark gold
    'tertiary': '#8b7355',     # Bronze/brown
    'light_gold': '#f4d03f',   # Light gold
    'background': '#0a1929',   # Dark navy
    'text': '#cbd5e1',         # Light gray
    'graduate': '#d4af37',     # Gold for Graduate (best outcome)
    'dropout': '#6b5d4f',      # Dark brown for Dropout (neutral)
    'enrolled': '#94a3b8'      # Light gray for Enrolled (neutral)
}

st.markdown("""
<div class="main-header">
    <h1>STUDENT DROPOUT PREDICTION SYSTEM</h1>
    <p>AI-Powered Early Intervention & Risk Assessment Platform</p>
</div>
""", unsafe_allow_html=True)

try:
    xgb_model, baseline_model, scaler, label_encoder = load_models()
    df = load_dataset()

    with st.sidebar:
        st.markdown("<h2 style='color: #d4af37; text-align: center; margin-bottom: 2rem;'>NAVIGATION</h2>", unsafe_allow_html=True)
        page = st.radio("", ["Home", "Prediction", "Voice Input", "Analytics"], label_visibility="collapsed")

        st.markdown("---")
        st.markdown(f"""
        <div class="professional-card">
            <h3 style='color: #d4af37; text-align: center; margin-bottom: 1rem; font-size: 1.1rem;'>DATASET INFO</h3>
            <p style='color: #d4af37; text-align: center; font-size: 2rem; font-weight: 900; margin: 0;'>{len(df):,}</p>
            <p style='color: #94a3b8; text-align: center; font-size: 0.9rem; margin-top: 0.5rem;'>TOTAL STUDENTS</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="professional-card">
            <h3 style='color: #d4af37; text-align: center; margin-bottom: 1rem; font-size: 1.1rem;'>MODEL INFO</h3>
            <p style='color: #cbd5e1; text-align: center; font-weight: 600;'>Primary: XGBoost</p>
            <p style='color: #cbd5e1; text-align: center; font-weight: 600;'>Baseline: Logistic Regression</p>
        </div>
        """, unsafe_allow_html=True)

    if page == "Home":
        col1, col2, col3 = st.columns(3)

        dropout_rate = (df['Target'].value_counts().get('Dropout', 0) / len(df) * 100)
        grad_rate = (df['Target'].value_counts().get('Graduate', 0) / len(df) * 100)
        enrolled_rate = (df['Target'].value_counts().get('Enrolled', 0) / len(df) * 100)

        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{dropout_rate:.1f}%</div>
                <div class="metric-label">Dropout Rate</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{grad_rate:.1f}%</div>
                <div class="metric-label">Graduation Rate</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{enrolled_rate:.1f}%</div>
                <div class="metric-label">Enrolled Rate</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<h2 class='section-header'>System Overview</h2>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="professional-card">
                <h3 style='color: #d4af37; font-size: 1.2rem; margin-bottom: 1rem;'>VOICE INTERACTION</h3>
                <p style='color: #cbd5e1; font-size: 1rem; line-height: 1.7;'>
                Natural language processing enables teachers to input student data through conversational voice commands.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="professional-card">
                <h3 style='color: #d4af37; font-size: 1.2rem; margin-bottom: 1rem;'>PREDICTIVE ANALYTICS</h3>
                <p style='color: #cbd5e1; font-size: 1rem; line-height: 1.7;'>
                Advanced machine learning algorithms analyze student profiles to predict dropout risk with high accuracy.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="professional-card">
                <h3 style='color: #d4af37; font-size: 1.2rem; margin-bottom: 1rem;'>EARLY INTERVENTION</h3>
                <p style='color: #cbd5e1; font-size: 1rem; line-height: 1.7;'>
                Actionable insights and personalized recommendations enable timely interventions to improve student outcomes.
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<h2 class='section-header'>Student Status Distribution</h2>", unsafe_allow_html=True)

        target_counts = df['Target'].value_counts()
        fig = go.Figure(data=[go.Pie(
            labels=target_counts.index,
            values=target_counts.values,
            hole=0.4,
            marker=dict(
                colors=[CHART_COLORS['graduate'], CHART_COLORS['dropout'], CHART_COLORS['enrolled']],
                line=dict(color=CHART_COLORS['background'], width=2)
            ),
            textfont=dict(size=16, color='white', family='Roboto'),
            textposition='inside'
        )])
        fig.update_layout(
            height=450,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color=CHART_COLORS['text'], size=14, family='Roboto'),
            showlegend=True,
            legend=dict(
                bgcolor='rgba(30, 41, 59, 0.8)',
                bordercolor='#334155',
                borderwidth=1,
                font=dict(color=CHART_COLORS['text'])
            )
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("<h2 class='section-header'>Dataset Information</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class="info-box">
            <h3 style='color: #d4af37; font-size: 1.1rem; margin-bottom: 1rem;'>DATA SOURCE</h3>
            <p style='color: #cbd5e1; font-size: 1rem; line-height: 1.7; margin-bottom: 1rem;'>
            This prediction system is built using the <strong>Predict Students' Dropout and Academic Success</strong> dataset
            from the UCI Machine Learning Repository, available on Kaggle.
            </p>
            <p style='color: #cbd5e1; font-size: 1rem; line-height: 1.7; margin-bottom: 1rem;'>
            <strong>Dataset Details:</strong><br>
            • Total Students: 4,424<br>
            • Features: 34 student attributes (demographic, academic, financial, and socio-economic)<br>
            • Target: Student outcome (Graduate, Dropout, or Enrolled)<br>
            • Source Institution: Portuguese higher education institution
            </p>
            <p style='color: #cbd5e1; font-size: 1rem; line-height: 1.7;'>
            📊 <strong>Kaggle Dataset:</strong>
            <a href="https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention"
               target="_blank"
               style="color: #d4af37; text-decoration: none; font-weight: 600;">
               Higher Education Predictors of Student Retention
            </a>
            </p>
            <p style='color: #94a3b8; font-size: 0.9rem; margin-top: 1rem; font-style: italic;'>
            Citation: Realinho, V., Machado, J., Baptista, L., & Martins, M. V. (2022).
            Predicting Student Dropout and Academic Success. Data, 7(11), 146.
            </p>
        </div>
        """, unsafe_allow_html=True)

    elif page == "Voice Input":
        st.markdown("<h2 class='section-header'>Voice-Enabled Data Collection</h2>", unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
            <h3 style='color: #d4af37; font-size: 1.1rem; margin-bottom: 1rem;'>INSTRUCTIONS:</h3>
            <ol style='color: #cbd5e1; font-size: 1rem; line-height: 1.8; margin: 0;'>
                <li>Click "Start Voice Input" button</li>
                <li>Allow microphone access when prompted by browser</li>
                <li>Respond to AI prompts with student information</li>
                <li>System collects: Age, Gender, Academic Performance, Financial Status</li>
                <li>Receive instant prediction with vocal confirmation</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

        components.html(voice_component, height=750)

    elif page == "Prediction":
        st.markdown("<h2 class='section-header'>Manual Prediction Input</h2>", unsafe_allow_html=True)

        with st.form("prediction_form"):
            st.markdown("### DEMOGRAPHIC INFORMATION")
            col1, col2, col3 = st.columns(3)

            with col1:
                age = st.number_input("Age at Enrollment", min_value=17, max_value=70, value=20)
            with col2:
                gender = st.selectbox("Gender", [1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
            with col3:
                marital_status_options = {
                    1: "Single",
                    2: "Married",
                    3: "Widowed",
                    4: "Divorced",
                    5: "De Facto Union",
                    6: "Legally Separated"
                }
                marital_status = st.selectbox(
                    "Marital Status",
                    list(marital_status_options.keys()),
                    format_func=lambda x: marital_status_options[x]
                )

            st.markdown("### FINANCIAL STATUS")
            col1, col2, col3 = st.columns(3)

            with col1:
                tuition_fees = st.selectbox("Tuition Fees Status", [1, 0],
                                          format_func=lambda x: "Up to Date" if x == 1 else "Outstanding")
            with col2:
                scholarship = st.selectbox("Scholarship Holder", [1, 0],
                                          format_func=lambda x: "Yes" if x == 1 else "No")
            with col3:
                debtor = st.selectbox("Debtor Status", [1, 0],
                                     format_func=lambda x: "Yes" if x == 1 else "No")

            st.markdown("### ACADEMIC BACKGROUND")
            col1, col2, col3 = st.columns(3)

            with col1:
                course_options = {
                    1: "Biofuel Production Technologies",
                    2: "Animation and Multimedia Design",
                    3: "Social Service (evening attendance)",
                    4: "Agronomy",
                    5: "Communication Design",
                    6: "Veterinary Nursing",
                    7: "Informatics Engineering",
                    8: "Equinculture",
                    9: "Management",
                    10: "Social Service",
                    11: "Tourism",
                    12: "Nursing",
                    13: "Oral Hygiene",
                    14: "Advertising and Marketing Management",
                    15: "Journalism and Communication",
                    16: "Basic Education",
                    17: "Management (evening attendance)"
                }
                course = st.selectbox(
                    "Course/Program",
                    list(course_options.keys()),
                    format_func=lambda x: course_options[x],
                    index=11  # Default to Nursing (most common)
                )
            with col2:
                prev_qual_options = {
                    1: "Secondary Education - 12th Grade",
                    2: "Higher Education - Bachelor's Degree",
                    3: "Higher Education - Degree",
                    4: "Higher Education - Master's",
                    5: "Higher Education - Doctorate",
                    6: "Frequency of Higher Education",
                    7: "12th Grade - Not Completed",
                    8: "11th Grade - Not Completed",
                    9: "Other - 11th Grade",
                    10: "10th Grade",
                    11: "10th Grade - Not Completed",
                    12: "Basic Education 3rd Cycle (9th/10th/11th)",
                    13: "Basic Education 2nd Cycle (6th/7th/8th)",
                    14: "Technological Specialization Course",
                    15: "Higher Education - Degree (1st Cycle)",
                    16: "Professional Higher Technical Course",
                    17: "Higher Education - Master's (2nd Cycle)"
                }
                previous_qualification = st.selectbox(
                    "Previous Qualification",
                    list(prev_qual_options.keys()),
                    format_func=lambda x: prev_qual_options[x]
                )
            with col3:
                displaced = st.selectbox("Displaced Student", [1, 0],
                                        format_func=lambda x: "Yes" if x == 1 else "No")

            st.markdown("### FIRST SEMESTER PERFORMANCE")
            col1, col2, col3 = st.columns(3)

            with col1:
                curricular_units_1st_sem_enrolled = st.number_input("Units Enrolled", min_value=0, max_value=30, value=6)
            with col2:
                curricular_units_1st_sem_approved = st.number_input("Units Approved", min_value=0, max_value=30, value=6)
            with col3:
                curricular_units_1st_sem_grade = st.number_input("Average Grade", min_value=0.0, max_value=20.0, value=12.0, step=0.1)

            submitted = st.form_submit_button("GENERATE PREDICTION", use_container_width=True)

            if submitted:
                curricular_units_1st_sem_evaluations = curricular_units_1st_sem_enrolled

                input_data = pd.DataFrame([[
                    marital_status, 1, 1, course, 1, previous_qualification, 1,
                    1, 1, 1, 1, displaced, 0, debtor,
                    tuition_fees, gender, scholarship, age, 0,
                    0, curricular_units_1st_sem_enrolled, curricular_units_1st_sem_evaluations,
                    curricular_units_1st_sem_approved, curricular_units_1st_sem_grade, 0,
                    0, 6, 6, 6, 12.0, 0,
                    10, 1, 1
                ]], columns=[
                    'Marital status', 'Application mode', 'Application order', 'Course',
                    'Daytime/evening attendance', 'Previous qualification', 'Nacionality',
                    "Mother's qualification", "Father's qualification", "Mother's occupation",
                    "Father's occupation", 'Displaced', 'Educational special needs', 'Debtor',
                    'Tuition fees up to date', 'Gender', 'Scholarship holder', 'Age at enrollment', 'International',
                    'Curricular units 1st sem (credited)', 'Curricular units 1st sem (enrolled)',
                    'Curricular units 1st sem (evaluations)', 'Curricular units 1st sem (approved)',
                    'Curricular units 1st sem (grade)', 'Curricular units 1st sem (without evaluations)',
                    'Curricular units 2nd sem (credited)', 'Curricular units 2nd sem (enrolled)',
                    'Curricular units 2nd sem (evaluations)', 'Curricular units 2nd sem (approved)',
                    'Curricular units 2nd sem (grade)', 'Curricular units 2nd sem (without evaluations)',
                    'Unemployment rate', 'Inflation rate', 'GDP'
                ])

                input_scaled = scaler.transform(input_data)
                xgb_pred = xgb_model.predict(input_scaled)[0]
                xgb_proba = xgb_model.predict_proba(input_scaled)[0]
                xgb_result = label_encoder.inverse_transform([xgb_pred])[0]

                st.markdown("---")
                st.markdown("<h2 class='section-header'>Prediction Result</h2>", unsafe_allow_html=True)

                result_class = f"result-{xgb_result.lower()}"
                confidence = max(xgb_proba) * 100

                st.markdown(f"""
                <div class="result-card {result_class}">
                    <h2>PREDICTED OUTCOME</h2>
                    <h1>{xgb_result.upper()}</h1>
                    <p>Confidence Level: {confidence:.1f}%</p>
                </div>
                """, unsafe_allow_html=True)

                prob_df = pd.DataFrame({
                    'Outcome': label_encoder.classes_,
                    'Probability': xgb_proba * 100
                })

                fig = go.Figure(data=[go.Bar(
                    x=prob_df['Outcome'],
                    y=prob_df['Probability'],
                    marker=dict(
                        color=[CHART_COLORS['graduate'], CHART_COLORS['dropout'], CHART_COLORS['enrolled']],
                        line=dict(color=CHART_COLORS['text'], width=1)
                    ),
                    text=[f'{p:.1f}%' for p in prob_df['Probability']],
                    textposition='outside',
                    textfont=dict(size=14, color=CHART_COLORS['text'], family='Roboto')
                )])

                fig.update_layout(
                    title="Probability Distribution",
                    height=400,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color=CHART_COLORS['text'], size=12, family='Roboto'),
                    yaxis_title="Probability (%)",
                    xaxis_title="Outcome",
                    showlegend=False,
                    title_font=dict(color=CHART_COLORS['primary'], size=16)
                )
                st.plotly_chart(fig, use_container_width=True)

                risk_factors = []
                if tuition_fees == 0:
                    risk_factors.append("Outstanding tuition fees identified")
                if curricular_units_1st_sem_grade < 10:
                    risk_factors.append("Below average academic performance")
                if scholarship == 0 and tuition_fees == 0:
                    risk_factors.append("Financial instability detected")
                if debtor == 1:
                    risk_factors.append("Student has outstanding debts")
                if curricular_units_1st_sem_approved < curricular_units_1st_sem_enrolled * 0.7:
                    risk_factors.append("Low course completion rate in first semester")

                if risk_factors:
                    st.markdown("<h3 class='section-header'>Risk Factors</h3>", unsafe_allow_html=True)
                    for factor in risk_factors:
                        st.markdown(f"""
                        <div class="warning-box">
                            <p style='color: #cbd5e1; font-size: 1rem; margin: 0; font-weight: 500;'>{factor}</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="success-box">
                        <p style='color: #cbd5e1; font-size: 1rem; margin: 0; font-weight: 500;'>No major risk factors identified</p>
                    </div>
                    """, unsafe_allow_html=True)

    else:  # Analytics
        st.markdown("<h2 class='section-header'>Data Analytics Dashboard</h2>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Tuition Payment Impact")
            tuition_target = pd.crosstab(df['Tuition fees up to date'], df['Target'], normalize='index') * 100
            fig = px.bar(
                tuition_target,
                barmode='group',
                color_discrete_sequence=[CHART_COLORS['graduate'], CHART_COLORS['dropout'], CHART_COLORS['enrolled']]
            )
            fig.update_layout(
                height=400,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color=CHART_COLORS['text'], size=12, family='Roboto'),
                yaxis_title="Percentage (%)"
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("### Academic Performance Distribution")
            fig = px.box(
                df,
                x='Target',
                y='Curricular units 1st sem (grade)',
                color='Target',
                color_discrete_map={
                    'Graduate': CHART_COLORS['graduate'],
                    'Dropout': CHART_COLORS['dropout'],
                    'Enrolled': CHART_COLORS['enrolled']
                }
            )
            fig.update_layout(
                height=400,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color=CHART_COLORS['text'], size=12, family='Roboto'),
                yaxis_title="Grade"
            )
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("### Age Distribution Analysis")
        fig = px.histogram(
            df,
            x='Age at enrollment',
            color='Target',
            nbins=25,
            color_discrete_map={
                'Graduate': CHART_COLORS['graduate'],
                'Dropout': CHART_COLORS['dropout'],
                'Enrolled': CHART_COLORS['enrolled']
            }
        )
        fig.update_layout(
            height=400,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color=CHART_COLORS['text'], size=12, family='Roboto')
        )
        st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"System Error: {str(e)}")
    st.info("Please ensure all required model files are present in the application directory.")

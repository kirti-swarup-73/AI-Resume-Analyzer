import "./App.css";
import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [resumeText, setResumeText] = useState("");
  const [analysis, setAnalysis] = useState("");

  const uploadResume = async () => {
    if (!file) {
      alert("Please select a resume file");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:5000/upload",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      alert("Resume Uploaded Successfully");

      setResumeText(data.resume_text);
    } catch (error) {
      alert("Upload Failed");
      console.log(error);
    }
  };

  const analyzeResume = async () => {
    if (!jobDescription) {
      alert("Please enter a Job Description");
      return;
    }

    try {
      setAnalysis("Analyzing Resume...");

      const response = await fetch(
        "http://127.0.0.1:5000/analyze",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            jobDescription,
          }),
        }
      );

      const data = await response.json();

      if (data.error) {
        setAnalysis(data.error);
        return;
      }

      if (data.analysis) {
        setAnalysis(data.analysis);
      } else {
        setAnalysis(JSON.stringify(data, null, 2));
      }

    } catch (error) {
      alert("Analysis Failed");
      console.log(error);
    }
  };

  return (
    <div className="container">

      <h1 className="title">
        AI Resume Analyzer
      </h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <textarea
        className="input-box"
        placeholder="Paste Job Description Here..."
        rows="8"
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />

      <div className="button-group">
        <button
          className="btn"
          onClick={uploadResume}
        >
          Upload Resume
        </button>

        <button
          className="btn"
          onClick={analyzeResume}
        >
          Analyze Resume
        </button>
      </div>

      {resumeText && (
        <div className="resume-preview">
          <h2>Resume Preview</h2>

          <textarea
            value={resumeText}
            rows="12"
            readOnly
          />
        </div>
      )}

      {analysis && (
        <div className="card">
          <h2>Analysis Result</h2>

          <pre
            style={{
              whiteSpace: "pre-wrap",
            }}
          >
            {analysis}
          </pre>
        </div>
      )}

    </div>
  );
}

export default App;
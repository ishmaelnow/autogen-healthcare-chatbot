// src/api/consult.js
import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

export const consult = async (symptom) => {
  try {
    console.log("Sending symptom to backend:", symptom);
    const res = await axios.post(`${API_BASE}/consult`, { symptom });
    console.log("Backend response:", res.data);

    const data = res.data.response;
    if (typeof data === "object" && data !== null) {
      // show only the summary field or stringify as fallback
      return data.summary || JSON.stringify(data);
    }
    return data;
  } catch (err) {
    console.error("Error contacting backend:", err);
    throw new Error("Error contacting backend");
  }
};

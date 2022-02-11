const API_URL = "http://127.0.0.1:8000/api/Checklist/Ver/"

export const listChecklist= async ()=>{
    return await fetch(API_URL);
};
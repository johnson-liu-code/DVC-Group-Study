import React, { useEffect, useState } from 'react'
const API = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export default function Tutor(){
  const [reqs, setReqs] = useState<any[]>([])
  useEffect(()=>{ fetch(`${API}/tutor/requests`).then(r=>r.json()).then(setReqs).catch(()=>setReqs([])) },[])
  return (
    <div>
      <h2>Tutor — Requests</h2>
      {reqs.length===0 ? <div>No requests.</div> : (
        <ul>{reqs.map(r=>(<li key={r.id}>{r.location} — {new Date(r.start_at).toLocaleString()}</li>))}</ul>
      )}
    </div>
  )
}

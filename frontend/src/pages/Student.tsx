import React, { useEffect, useState } from 'react'
const API = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export default function Student(){
  const [groups, setGroups] = useState<any[]>([])
  useEffect(()=>{ fetch(`${API}/groups`).then(r=>r.json()).then(setGroups).catch(()=>setGroups([])) },[])
  return (
    <div>
      <h2>Student — Browse & Join</h2>
      <p><em>Public groups show participant initials before you join.</em></p>
      <div style={{display:'grid', gap:8}}>
        {groups.map(g=>(
          <div key={g.id} style={{border:'1px solid #ddd', padding:8, borderRadius:8}}>
            <div><strong>{g.title}</strong> ({g.course_code})</div>
            <div>Participants: {g.participant_initials?.join(' ') || '—'}</div>
            <div>Tutor requested: {g.tutor_requested ? 'Yes' : 'No'}</div>
          </div>
        ))}
      </div>
    </div>
  )
}

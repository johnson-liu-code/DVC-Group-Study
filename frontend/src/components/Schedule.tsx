import React from 'react'

export default function Schedule({items}:{items:any[]}){
  if(!items?.length) return <div>No sessions scheduled.</div>
  return (
    <div style={{display:'grid', gap:8}}>
      {items.map((s:any)=>(
        <div key={s.id} style={{border:'1px solid #ccc', padding:8, borderRadius:8}}>
          <div><strong>{new Date(s.start_at).toLocaleString()} - {new Date(s.end_at).toLocaleString()}</strong></div>
          <div>Location: {s.location} {s.room_id ? `(Room ${s.room_id})` : ''}</div>
          <div>Status: {s.status}</div>
        </div>
      ))}
    </div>
  )
}

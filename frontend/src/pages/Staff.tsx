import React, { useEffect, useState } from 'react'
import Schedule from '../components/Schedule'
const API = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export default function Staff(){
  const [items, setItems] = useState<any[]>([])
  useEffect(()=>{ fetch(`${API}/admin/schedule`).then(r=>r.json()).then(setItems).catch(()=>setItems([])) },[])
  return (
    <div>
      <h2>Staff — Schedule (Tutoring Center)</h2>
      <Schedule items={items} />
    </div>
  )
}

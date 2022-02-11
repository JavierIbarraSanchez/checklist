import React, { useEffect, useState } from "react";
import * as CheckListServer from "./ChecListServer"
const Checklist = () => {
 
  const [checklist, crearchecklist] = useState([]);

  const listChecklist =()=>{
      try {
          const res = CheckListServer.listChecklist()
      } catch (error) {
          console.log(error);
      }
  }

  useEffect(()=> {
    listChecklist();
  },[]);
  return (
    <div>
      {checklist.map((checklist) => (
        <h2>{checklist.nombre_checklist}</h2>
      ))}
    </div>
  );
};

export default Checklist;

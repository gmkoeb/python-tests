import { useState } from "react"
import './App.css'

function App() {
  const [plot, setPlot] = useState('')
  const [formFile, setFormFile] = useState('Drag and drop a txt file here or')
  async function handleUpload(event){
    event.preventDefault()
    const dataInput = document.getElementById('dataUpload')
    const formData = new FormData()
    const file = dataInput.files[0]
    formData.append('file', file)
  
    const uploadResponse = await fetch('http://localhost:5000/fit', {
      method: 'POST',
      body: formData
    })
  
    const imageBlob = await uploadResponse.blob()
    const imageURL = URL.createObjectURL(imageBlob)
    setPlot(imageURL)
  }

  function handleDragover(event){
    event.preventDefault()
  }

  function handleFormChange(event){
    event.preventDefault()
    const fileInput = document.getElementById('dataUpload')
    if (event._reactName === 'onDrop'){
      const file = event.dataTransfer.files
      fileInput.files = file
      setFormFile(file[0].name)
    }else{
      setFormFile(fileInput.files[0].name)
    }
  }

  return (
    <main>
      <h1>Fitter</h1>
      <form onChange={handleUpload} onDrop={handleUpload}>
        <div id="dropContainer">
          <label id="fileField" onDrop={handleFormChange} onDragOver={handleDragover} htmlFor="dataUpload">
            <p>{formFile}</p>
            <label id="uploadSelect" htmlFor="dataUpload">browse</label>
            <input type="file" name="dataUpload" id="dataUpload"></input>
          </label>
        </div>
      </form>
      <img src={`${plot}`} alt="" />
    </main>
  )
}

export default App;

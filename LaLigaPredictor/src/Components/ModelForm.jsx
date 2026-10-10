import generatePDF from '../Services/jsPDF'
import {React, useRef} from 'react'
import './ModelForm.css'
import Barcelona from '../Crests/FC_Barcelona.svg'
import AthleticClub from '../Crests/athletic-bilbao.svg'
import AtleticoMadrid from '../Crests/atltico-madrid.svg'
import CeltaVigo from '../Crests/Celta_Vigo.svg'
import Alaves from '../Crests/Deportivo_Alaves.svg'
import Elche from '../Crests/Elche_CF.svg'
import Espanyol from '../Crests/RCD_Espanyol.svg'
import Getafe from '../Crests/Getafe_CF.svg'
import Girona from '../Crests/girona-fc.svg'
import Levante from '../Crests/levante-ud.svg'
import Osasuna from '../Crests/CA_Osasuna.svg'
import RayoVallecano from '../Crests/Rayo_Vallecano.svg'
import RealBetis from '../Crests/Real_Betis.svg'
import RealMadrid from '../Crests/Real_Madrid.svg'
import RealSociedad from '../Crests/real-sociedad.svg'
import Sevilla from '../Crests/Sevilla_FC.svg'
import Valencia from '../Crests/valencia-cf.svg'
import Villarreal from '../Crests/Villarreal_CF.svg'
import RealOviedo from '../Crests/real-oviedo.svg'
import Mallorca from '../Crests/RCD_Mallorca.svg'

const teamCrests = {
    Barcelona: Barcelona,
    "real-oviedo": RealOviedo,
    "rcd-mallorca": Mallorca,
    alaves: Alaves,
    "athletic-club": AthleticClub,
    "atletico-madrid": AtleticoMadrid,
    "celta-vigo": CeltaVigo,
    elche: Elche,
    espanyol: Espanyol,
    getafe: Getafe,
    girona: Girona,
    levante: Levante,
    osasuna: Osasuna,
    "rayo-vallecano": RayoVallecano,
    "real-betis": RealBetis,
    RealMadrid: RealMadrid,
    "real-sociedad": RealSociedad,
    sevilla: Sevilla,
    valencia: Valencia,
    villarreal: Villarreal
}

const pdfContent = {}

function ModelForm(){

    const imgRef = useRef(null)

    const handleTeamSelection = (event) => {
        const selectedTeam = event.target.value
        imgRef.current.src = teamCrests[selectedTeam]
        pdfContent.teamLogo = selectedTeam
        console.log(pdfContent)
    }

    return (
        <div id="model-form-div">
            <div id="model-form">
                <div id="form-container">
                    <form className="model-forms" action="">
                        <input type="number" max="100" min="0" step={0.1} placeholder="Enter xG Socored per match"></input>
                        <input type="number" max="100" min="0" step={0.1} placeholder="Enter xG Conceded per match"></input>
                        <input type="number" max="100" min="0" step={0.1} placeholder="Enter Goals Scored per match"></input>
                        <input type="number" max="100" min="0" step={0.1} placeholder="Enter Goals Conceded per match"></input>
                    </form>
                    <form className="model-forms" action="">
                        <input type="number" max="100" min="0" step={1} placeholder="Enter Clean Sheets Percentage"></input>
                        <input type="number" max="100" min="0" step={1} placeholder="Enter Failed to Score Percentage"></input>
                        <input type="number" max="100" min="0" step={1} placeholder="Enter Possession AVG"></input>
                    </form>
                </div>
                <button onClick={() => generatePDF(pdfContent)} id="predict-button">Predict</button>
            </div>
            <div id="Team-Selection">
                <select name="team-selection" id="team-selection" defaultValue="Barcelona" onChange={handleTeamSelection}>
                    <option value="Barcelona">FC Barcelona</option>
                    <option value="alaves">Deportivo Alavés</option>
                    <option value="athletic-club">Athletic Club</option>
                    <option value="atletico-madrid">Atlético de Madrid</option>
                    <option value="celta-vigo">RC Celta de Vigo</option>
                    <option value="deportivo">RC Deportivo de La Coruña</option>
                    <option value="elche">Elche CF</option>
                    <option value="espanyol">RCD Espanyol</option>
                    <option value="getafe">Getafe CF</option>
                    <option value="girona">Girona FC</option>
                    <option value="levante">Levante UD</option>
                    <option value="osasuna">CA Osasuna</option>
                    <option value="rayo-vallecano">Rayo Vallecano</option>
                    <option value="real-betis">Real Betis</option>
                    <option value="RealMadrid">Real Madrid</option>
                    <option value="real-sociedad">Real Sociedad</option>
                    <option value="sevilla">Sevilla FC</option>
                    <option value="valencia">Valencia CF</option>
                    <option value="villarreal">Villarreal CF</option>
                </select>
                <img ref={imgRef} src={Barcelona} alt="Team Logo" id="team-logo" />
            </div>
        </div>        
    )
}

export default ModelForm;
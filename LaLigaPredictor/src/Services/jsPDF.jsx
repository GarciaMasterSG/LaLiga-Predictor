import jsPDF from 'jspdf';
import "svg2pdf.js";
import Barcelona from '../Crests/FC_Barcelona.png'
import AthleticClub from '../Crests/athletic-bilbao.png'
import AtleticoMadrid from '../Crests/atltico-madrid.png'
import CeltaVigo from '../Crests/Celta_Vigo.png'
import Alaves from '../Crests/Deportivo_Alaves.png'
import Elche from '../Crests/Elche_CF.png'
import Espanyol from '../Crests/RCD_Espanyol.png'
import Getafe from '../Crests/Getafe_CF.png'
import Girona from '../Crests/girona-fc.png'
import Levante from '../Crests/levante-ud.png'
import Osasuna from '../Crests/CA_Osasuna.png'
import RayoVallecano from '../Crests/Rayo_Vallecano.png'
import RealBetis from '../Crests/Real_Betis.png'
import RealMadrid from '../Crests/Real_Madrid.png'
import RealSociedad from '../Crests/real-sociedad.png'
import Sevilla from '../Crests/Sevilla_FC.png'
import Valencia from '../Crests/valencia-cf.png'
import Villarreal from '../Crests/Villarreal_CF.png'
import RealOviedo from '../Crests/real-oviedo.png'
import Mallorca from '../Crests/RCD_Mallorca.png'

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


const generatePDF = async (content) => {
    const doc = new jsPDF();

    const width = doc.internal.pageSize.getWidth();
    const height = doc.internal.pageSize.getHeight();

    // ==========================================
    // HEADER
    // ==========================================

    doc.setFontSize(24);
    doc.setFont("Helvetica", "bold");
    doc.text("LaLiga Predictor", 20, 25);

    doc.setFontSize(12);
    doc.setFont("Helvetica", "normal");
    doc.text("Team Position Prediction Report", 20, 33);

    // Team crest
    doc.addImage(
        teamCrests[content.teamLogo],
        "PNG",
        width - 60,
        10,
        50,
        50
    );

    // Divider
    doc.line(20, 65, width - 20, 65);


    // ==========================================
    // TEAM INFORMATION
    // ==========================================

    doc.setFontSize(16);
    doc.setFont("Helvetica", "bold");
    doc.text("Team Information", 20, 80);

    doc.setFontSize(13);
    doc.setFont("Helvetica", "normal");
    doc.text(`Team: ${content.teamLogo.toUpperCase()}`, 20, 90);


    // ==========================================
    // INPUT STATISTICS
    // ==========================================

    doc.setFontSize(16);
    doc.setFont("Helvetica", "bold");
    doc.text("Input Statistics", 20, 110);


    // Statistics boxes
    const boxWidth = 80;
    const boxHeight = 22;

    // Row 1
    doc.rect(20, 118, boxWidth, boxHeight);
    doc.rect(110, 118, boxWidth, boxHeight);

    doc.setFontSize(10);
    doc.setFont("Helvetica", "normal");

    doc.text("xG Scored / Match", 24, 126);
    doc.text(`${30}`, 24, 135);

    doc.text("xG Conceded / Match", 114, 126);
    doc.text(`${30}`, 114, 135);


    // Row 2
    doc.rect(20, 145, boxWidth, boxHeight);
    doc.rect(110, 145, boxWidth, boxHeight);

    doc.text("Goals Scored / Match", 24, 153);
    doc.text(`${30}`, 24, 162);

    doc.text("Goals Conceded / Match", 114, 153);
    doc.text(`${30}`, 114, 162);


    // Row 3
    doc.rect(20, 172, boxWidth, boxHeight);
    doc.rect(110, 172, boxWidth, boxHeight);

    doc.text("Clean Sheets", 24, 180);
    doc.text(`${20}%`, 24, 189);

    doc.text("Failed to Score", 114, 180);
    doc.text(`${30}%`, 114, 189);


    // Row 4
    doc.rect(20, 199, 170, boxHeight);

    doc.text("Possession Average", 24, 207);
    doc.text(`${20}%`, 24, 216);


    // ==========================================
    // PREDICTION
    // ==========================================

    doc.setFontSize(16);
    doc.setFont("Helvetica", "bold");
    doc.text("Predicted Position", 20, 235);

    // Big prediction box
    doc.rect(65, 242, 80, 35);

    doc.setFontSize(30);
    doc.setFont("Helvetica", "bold");

    doc.text(
        `${400}`,
        width / 2,
        265,
        { align: "center" }
    );

    doc.setFontSize(10);
    doc.setFont("Helvetica", "normal");

    doc.text(
        "Predicted LaLiga Position",
        width / 2,
        273,
        { align: "center" }
    );


    // ==========================================
    // SHAP ANALYSIS
    // ==========================================

    doc.addPage();

    doc.setFontSize(16);
    doc.setFont("Helvetica", "bold");
    doc.text("SHAP Analysis", 20, 25);

    // SHAP container
    doc.rect(
        20,
        35,
        width - 40,
        240
    );


    // ==========================================
    // SAVE
    // ==========================================

    doc.save("LaLiga-Prediction.pdf");
};

export default generatePDF;
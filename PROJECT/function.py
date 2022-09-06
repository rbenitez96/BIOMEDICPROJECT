import joblib
import pandas as pd
# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')

AnemiaTypes = {"ACD":"Anemia por enfermedad crónica","IDA":"Anemia por deficiencia de hierro","ARD":"Anemia por enfermedad renal","THAL":"Talasemia","APA":"Anemia aplásica"}

def islowRDW(rdw):
  if(rdw >= 11 and rdw <= 16):
    return True
  elif(rdw < 11):
    return True
  return False

def ishgblow(hgb, sex): #sex:1 hombre, sex:0 mujer
  if (sex == 0):
    if(hgb >= 10.5 and hgb < 12.5):
      return "moderado"
    elif(hgb < 10.5):
      return "severo"
    return ""
  else:
    if(hgb >= 12 and hgb < 14):
      return "moderado"
    elif(hgb < 12):
      return "severo"
    return ""

def ismchclow(mchc):
  if(mchc >= 27 and mchc <= 34):
    return True
  elif(mchc < 27):
    return True
  return False

def ismcvrange(mcv):
  if(mcv >= 80 and mcv <= 100):
      return False
  return True

def obtener_interpretacion(dataframePaciente,lHGBpredicciones):
  indicepred = 0
  lista_resultados = []
  for datapaciente in dataframePaciente.to_numpy():
    sex = int(datapaciente[1])
    mcv = float(datapaciente[4])
    mchc = float(datapaciente[6])
    rdw = float(datapaciente[7])
    hgbpred = float(lHGBpredicciones[indicepred])
    indicepred += 1
    if(mcv < 80 and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="moderado"):
      texto = AnemiaTypes["ACD"]
      texto += " moderado"
    elif(mcv < 80 and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="severo"):
      texto = AnemiaTypes["ACD"]
      texto += " severo"
    elif(ismcvrange(mcv) and (mchc >= 27 and mchc <= 34) and islowRDW(rdw) and  ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="moderado"):
      texto = AnemiaTypes["THAL"]
      texto += " moderado"
    elif(ismcvrange(mcv) and (mchc < 27) and islowRDW(rdw) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="severo"):
      texto = AnemiaTypes["THAL"]
      texto += " severo"
    elif(ismcvrange(mcv) and (mchc >= 27 and mchc <= 34) and not(islowRDW(rdw)) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="moderado"):
      texto = AnemiaTypes["IDA"]
      texto += " moderado"
    elif(ismcvrange(mcv) and (mchc < 27) and not(islowRDW(rdw)) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="severo"):
      texto = AnemiaTypes["IDA"]
      texto += " severo"
    elif(ismcvrange(mcv) and (mchc >= 27 and mchc <= 34) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="moderado"):
      texto = AnemiaTypes["ARD"]
      texto += " moderado"
    elif(ismcvrange(mcv) and (mchc < 27) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="severo"):
      texto = AnemiaTypes["ARD"]
      texto += " severo"
    elif((mcv > 100) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="moderado"):
      texto = AnemiaTypes["APA"]
      texto += " moderado"
    elif((mcv > 100) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="severo"):
      texto = AnemiaTypes["APA"]
      texto += " severo"
    else:
      texto = "Sin anemia"
    
    texto2 = ""
    if(mcv < 80 and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="moderado" and (texto!="Sin anemia")):
      texto2 += AnemiaTypes["ACD"]
      texto2 += " moderado /"
    if(mcv < 80 and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="severo" and (texto!="Sin anemia")):
      texto2 += AnemiaTypes["ACD"]
      texto2 += " severo /"
    if(ismcvrange(mcv) and ismchclow(mchc) and islowRDW(rdw) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="moderado" and (texto!="Sin anemia")):
      texto2 += AnemiaTypes["THAL"]
      texto2 += " moderado /"
    if(ismcvrange(mcv) and ismchclow(mchc) and islowRDW(rdw) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="severo" and (texto!="Sin anemia")):
      texto2 += AnemiaTypes["THAL"]
      texto2 += " severo /"
    if(ismcvrange(mcv) and ismchclow(mchc) and not(islowRDW(rdw)) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="moderado" and (texto!="Sin anemia")):
      texto2 = AnemiaTypes["IDA"]
      texto2 += " moderado /"
    if(ismcvrange(mcv) and ismchclow(mchc) and not(islowRDW(rdw)) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="severo" and (texto!="Sin anemia")):
      texto2 = AnemiaTypes["IDA"]
      texto2 += " severo /"
    if(ismcvrange(mcv) and ismchclow(mchc) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="moderado" and (texto!="Sin anemia")):
      texto2 = AnemiaTypes["ARD"]
      texto2 += " moderado /"
    if(ismcvrange(mcv) and ismchclow(mchc) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="severo" and (texto!="Sin anemia")):
      texto2 = AnemiaTypes["ARD"]
      texto2 += " severo /"
    if((mcv > 100) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="moderado" and (texto!="Sin anemia")):
      texto2 = AnemiaTypes["APA"]
      texto2 += " moderado /"
    if((mcv > 100) and ishgblow(hgbpred,sex)!="" and ishgblow(hgbpred,sex)=="severo" and (texto!="Sin anemia")):
      texto2 = AnemiaTypes["APA"]
      texto2 += " severo /"
    if(texto=="Sin anemia"):
       texto2 = texto

    lista_resultados.append(texto2)
  return lista_resultados 

def loadmodel(namemodel):
    model_anemia_load = joblib.load(namemodel)
    return model_anemia_load

def predictmodel_anemia(namemodel,arregloData):
    DataframeUs = pd.DataFrame(arregloData)
    model_anemia_load = loadmodel(namemodel)
    hgbpredict = model_anemia_load.predict(DataframeUs)
    print(hgbpredict)
    lista_interpretacionespac = obtener_interpretacion(DataframeUs,hgbpredict)
    return lista_interpretacionespac[0]

def predictmodel_cancermama(namemodel,arregloData):
    DataframeUs = pd.DataFrame(arregloData)
    print(DataframeUs)
    model_cancermama_load = loadmodel(namemodel)
    iscancer = model_cancermama_load.predict(DataframeUs)
    #print(deteccionCancer(iscancer))
    return deteccionCancer(iscancer)
    

def deteccionCancer (Z_pred):
  respuesta = ""
  if  Z_pred[0] == 1:
    respuesta = "Usted tiene un cancer maligno"
  else:
    respuesta = "Usted tiene un cancer benigno"
  return respuesta





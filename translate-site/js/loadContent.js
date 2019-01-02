var urlParams = new URLSearchParams(window.location.search);
var languageId = urlParams.get('lang');

var title = document.getElementsByTagName('title')[0];
var cv = document.getElementById('cv');
var myName = document.getElementById('myName');
var siteTitle = document.getElementById('siteTitle');

if (languageId && languageId != 'en' && availibleLanguages.indexOf(languageId) > -1){
  console.log('Translating to ' + languageId);
  AWS.config.region = awsRegion;
  AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: poolId,
  });
  var translate = new AWS.Translate();
  translator(cvText, languageId, [cv]);
  translator(pageTitle, languageId, [title, myName]);
  translator(siteName, languageId, [siteTitle]);
}
else {
  languageId = 'en';
  updateData(pageTitle, title);
  updateData(cvText, cv);
  updateData(pageTitle, myName);
  updateData(siteName, siteTitle);
}

document.getElementById(languageId).removeAttribute("href");
document.getElementById(languageId).style.color = '#fff';

with (cv.style) {
  backgroundColor = '#555555cf';
  padding = '20px 50px 20px 50px';
}

if (languageId == 'he') {
  cv.style.direction = "rtl";
}

function translator(text, lang, element) {
  var params = {
  SourceLanguageCode: 'en',
  TargetLanguageCode: lang,
  Text: text,
  TerminologyNames: ['Boaz']
  };
  translate.translateText(params, function (err, data) {
    if (err) console.log(err, err.stack);
    else {
      console.log(data);
      element.forEach(function(name) {
        updateData(data.TranslatedText, name);
      });
    }
  });
}

function updateData(text, element) {
  element.innerText = text;
}

document.addEventListener("DOMContentLoaded", ready);

function ready() {
  $(".loader").fadeOut("slow");;
}

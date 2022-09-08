
function validate()
{
    const maxt = document.getElementById('maxt')
    const mint = document.getElementById('mint')
    const maxh = document.getElementById('maxh')
    const minh = document.getElementById('minh')
    const form = document.getElementById('addsessform')

        if (maxt.value <= mint.value){
            window.alert("Max value is smaller than min value");
            maxt.focus();
            return false;
        }

        if (maxh.value <= minh.value){
            window.alert("Max value is smaller than min value");
            maxh.focus();
            return false;
        }
        else{
            true;
        }
        
    
}

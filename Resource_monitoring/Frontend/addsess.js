
function validate()
{
    const maxt = document.getElementById('maxt')
    const mint = document.getElementById('mint')
    const maxh = document.getElementById('maxh')
    const minh = document.getElementById('minh')
    const form = document.getElementById('addsessform')

        if (maxt.value <= mint.value){
            window.alert("Max temperature value is smaller than min temperature value");
            maxt.focus();
            return false;
        }

        if (maxh.value <= minh.value){
            window.alert("Max humidity value is smaller than min humididty value");
            maxh.focus();
            return false;
        }
        else{
            true;
        }
        
    let newArray = [maxt,maxh,mint,minh];
    newArray.forEach((item)=>{
        var li = document.createElement("li");
    var text = document.createElement(item);
    li.appendChild(text);
    table.appendChild(li);    
    })
    form.reset();
}


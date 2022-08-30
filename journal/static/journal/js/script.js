function checkAmount (){
    document.addEventListener("DOMContentLoaded", function(){
        document.getElementById('submit').addEventListener('click', function(){
            var je1Debit = document.getElementById("je1-debit").value
            var je1Credit = document.getElementById("je1-credit").value
            var je2Debit = document.getElementById("je2-debit").value
            var je2Credit = document.getElementById("je2-credit").value
            
            var debitAmount = parseInt(je1Debit) + parseInt(je2Debit);
            var creditAmount = parseInt(je1Credit) + parseInt(je2Credit);
            if (debitAmount != creditAmount) {
                alert("貸借不一致");
            } else {
                return true
            }
        });
    }, false);
};
// https://teratail.com/questions/24714


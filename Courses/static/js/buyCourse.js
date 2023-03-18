//BuyCourse
        const buyBtns=document.querySelectorAll('.js-btnbuy')
        const model=document.querySelector('.js-model')
        const container=document.querySelector('.js-container')
        const exit=document.querySelector('.js-exit')
        function showBuyTickets(){
            model.classList.add('open')
        }
        function hideBuyTickets(){
            model.classList.remove('open')
        }
        for(const buyBtn of buyBtns){
            buyBtn.addEventListener('click',showBuyTickets)
        }
        exit.addEventListener('click',hideBuyTickets)
        model.addEventListener('click',hideBuyTickets)
        container.addEventListener('click',function(event){
            event.stopPropagation()
        })

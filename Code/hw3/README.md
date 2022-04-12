Q1:

Part1:
    The controller defines the necessary information for each state:
        - current floor {0,1,2,3}
        - current array of open doors, initially [FALSE, FALSE, FALSE, FALSE]
        - current array of buttons, controlled by the environment 
        - currently served request: req1, takes on the values -1..3. "-1" means no request
        - cached request: req2, takes on the values -1..3
        - time since floor 0 was requested: timer, takes on the values 0..2

    We satisfy the first spec, "A requested floor will be served some time", by serving req1. To "serve req1" is to go to its requested floor and open the door. Once this occurs, req1 is set to the cached request (req2) if it has a requested floor (i.e. req2!=-1), otherwise it is set to any any button that is TRUE, or back to -1. 
        - the mechanism for moving to a floor is straightforward: move in the direction of the requested floor (req1) until floor=req1. Then, open the door. 

    We satisfy the second spec, "Again and again the elevator returns to floor 0", using the timer variable. The timer variable is the number of consecutive steps where req1!=0 & req2!=0, and caps at a value of 2. Once the timer reaches 2, req2 will be set to 0 at the next available step. This ensures that we will always return to floor 0. This does mean that, if no buttons are pressed, the door will infinitely stay open on the bottom floor, which is probably an odd behavior for the real world.

    I included an additional spec, "A door cannot be open unless the elevator is at its floor" (e.g. doors[0]=TRUE -> (floor=0 & !doors[1] & !doors[2] & !doors[3])), as a sanity check to ensure our doors are "safe".

Part 2: 

    To satisfy the third spec, "When the top floor is requested, the elevator serves it immediately and does not stop on the way there.", I forced all third floor requests to be in req1 (i.e., G(req2!=3) ). While this does mean that we cannot cache a top floor request, it is a restriction that my controller needed to be able to guarantee we would always serve it first. In essence, this restricts how often the top floor can be requested, since it requires (req1=-1 & req2=-1 & buttons[3]=TRUE) for the top floor to be requested. To partially alleviate this restriction, the controller prioritizes requests to the top floor: if buttons[3]=TRUE and req1 is empty, then regardless of which other buttons were pressed, req1 will select floor 3 to serve. 


Results: satisfies all specs
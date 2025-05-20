let p = 4;       // |@0x01 p = 4;     // | move, NOP , 0x01, 4
@right v = &p;   // |@DAX v = &p;     // | move, NOP , DAX , 1
v -> @indirect;  // |v -> @IAX;       // | OP  , NOP , DAX , DAX , OAX
                 //                   // | move, OAX , IAX
if *v == 4:      // |if *v == 4:      // | ...
    *v = 3;      // |    *v = 3;      // | move, NOP , DAX , 3
                 //                   // | OP  , NOP , DAX , DAX , OAX
                 //                   // | pnt , WRT , IAX , OAX
v = v + 1;       // |@OAX o = v + 1;  // | pnt , MOVE, IAX , DAX
                 // |o -> @0x01; -> v // | move, NOP , DBX , 1
                                      // | OP  , ADD , DAX , DBX , OAX
                                      // | move, OAX , IAX
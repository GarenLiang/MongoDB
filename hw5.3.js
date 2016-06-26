# MongoDB
db.grades.aggregate([
                        { 
                          $unwind : "$scores" 
                        },
                        { 
                          $match: { 
                                    $or: [
                                            {"scores.type":"exam"},
                                            {"scores.type":"homework"}
                                         ]
                                  }
                        },
                        { 
                          $group: { 
                                    _id:{ 
                                            class_id: "$class_id",
                                            student_id: "$student_id"
                                        },
                                    grade:{ 
                                             $avg: "$scores.score"
                                          }
                                   }
                        },
                        { 
                          $group: {
                                    _id:{
                                            class_id: "$_id.class_id"
                                         },
                                   avg_grade:{
                                            $avg: "$grade"
                                             }
                                  }
                        },
                        { 
                                 $sort: { avg_grade : -1 }
                        },
                        {
                                 $limit:1
                        }
           ]).pretty()

# MongoDB
db.posts.aggregate
([{$unwind: "$comments"}, 
    {$group: 
       { "_id": "$comments.author", 
          "Total": {$sum:1}}},
  {$sort: {"Total": -1}}])

# Mini-batch

Rank 365. Type: concept. Tier: lighter.

## Checked
- LeCun, Bottou, Orr and Müller, *Efficient BackProp* (1998), §4.1, author PDF: batch learning averages the gradient over the training set; stochastic learning uses one example; mini-batches start small and grow, and the batch size plays a role comparable to the learning rate.
- Hastie, Tibshirani and Friedman, pp. 396–397: batch updates sum over all cases, online updates use one case, and an epoch is one sweep. The Robbins–Monro step-size conditions are stated there for online learning.
- The six pair-gradients of {1,3,5,7} average to −4, and −11/3 is the gradient of {1,3,7}.

## Assumed
- The loss in the worked example is the average of half squared errors, so the gradient is the negative mean response at w=0.

## Disputed
- None. The bibliography key lecun1998 is the 1998 document-recognition paper, which was not the paper read for this page. The new key is lecun_efficient_backprop1998.

## Sources read
- Yann LeCun, Léon Bottou, Genevieve B. Orr and Klaus-Robert Müller, *Efficient BackProp*, in *Neural Networks: Tricks of the Trade*, Springer, 1998, §4.1, http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf
- Trevor Hastie, Robert Tibshirani and Jerome Friedman, *The Elements of Statistical Learning*, 2nd ed., §11.4, pp. 396–397.

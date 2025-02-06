/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let first = init;
    return{
        increment: function() {
            return ++first;
        },
        reset: function() {
            return first = init;
        },
        decrement: function() {
            return --first;
        }
    };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

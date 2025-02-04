var expect = function(val1) {
    return {
        toBe: function(val2) {
            if (val1 !== val2) throw new Error("Not Equal");
            return true;
        },
        notToBe: function(val3) {
            if (val1 === val3) throw new Error("Equal");
            return true;
        }
    };
};

// Example Usage
try {
    console.log(expect(5).toBe(5));   // ✅ true
    console.log(expect(5).notToBe(10)); // ✅ true
    console.log(expect(5).notToBe(5)); // ❌ Throws "Equal"
} catch (e) {
    console.error(e.message);
}

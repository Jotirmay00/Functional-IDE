// eslint-disable-next-line no-unused-vars
import React from 'react';
const Description = () => {
  const examples = [
    {
      input: { nums: [2, 7, 11, 15], target: 9 },
      output: [0, 1],
    },
    {
      input: { nums: [3, 2, 4], target: 6 },
      output: [1, 2],
    },
  ];

  return (
    <div className="mb-4 overflow-y-auto">
      <h2 className="text-xl font-semibold text-white">Description</h2>
      <p className="mt-4 text-white">
        Given an array of integers <b>nums</b> and an integer <b>target</b>, return indices of the two numbers such that they add up to <b>target</b>.
        You may assume that each input would have <b>exactly one solution</b>, and you may not use the same element twice.
        You can return the answer in any order.
      </p>
      <div className="mt-4">
        {examples.map((example, index) => (
          <div key={index} className="mt-4 text-white">
            <b>Example {index + 1}:</b>
            <br />
            <b>Input:</b> nums = {example.input.nums.join(', ')}, target = {example.input.target}
            <br />
            <b>Output:</b> {example.output.join(', ')}
            <br />
            <b>Explanation:</b> Since nums[{example.output[0]}] + nums[{example.output[1]}] == {example.input.target}, we return [{example.output[0]}, {example.output[1]}].
          </div>
        ))}
      </div>
    </div>
  );
};

export default Description;

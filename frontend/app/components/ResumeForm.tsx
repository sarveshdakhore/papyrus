"use client";
import React, { useState } from 'react';

interface Option {
  value: string;
  label: string;
}

const JobForm: React.FC = () => {
  const [skills, setSkills] = useState('');
  const [experience, setExperience] = useState('');
  const [jobRole, setJobRole] = useState('');

  const experienceOptions: Option[] = [
    { value: '1', label: '1 year' },
    { value: '2', label: '2 years' },
    // Add more options as needed
  ];

  const jobRoleOptions: Option[] = [
    { value: 'developer', label: 'Developer' },
    { value: 'designer', label: 'Designer' },
    // Add more options as needed
  ];

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Handle form submission logic here
    console.log('Skills:', skills);
    console.log('Experience:', experience);
    console.log('Job Role:', jobRole);
  };

  return (
    <div className="flex justify-center items-center mt-[10px] ">
        <form onSubmit={handleSubmit}>
        <div>
            <label htmlFor="skills" className='block text-[30px]'>Skills:</label>
            <input
            type="text"
            id="skills"
            className='block text-black w-full p-4  bg-[#5555e228] rounded-lg border-2 border-blue-500'
            value={skills}
            onChange={(e) => setSkills(e.target.value)}
            />
        </div>
        <div>
            <label htmlFor="experience" className='block'>Experience:</label>
            <select
            id="experience"
            className='block text-white w-full p-4  bg-[#5555e278] rounded-lg border-2 border-blue-500'
            value={experience}
            onChange={(e) => setExperience(e.target.value)}
            >
            {experienceOptions.map((option) => (
                <option key={option.value} value={option.value}>
                {option.label}
                </option>
            ))}
            </select>
        </div>
        <div>
            <label htmlFor="jobRole" className='block'>Job Role:</label>
            <select
            id="jobRole"
            value={jobRole}
            className='block text-white w-full p-4 bg-[#5555e278] rounded-lg border-2 border-blue-500'
            onChange={(e) => setJobRole(e.target.value)}
            >
            {jobRoleOptions.map((option) => (
                <option key={option.value} value={option.value}>
                {option.label}
                </option>
            ))}
            </select>
        </div>
        <button type="submit" className=' my-[10px] self-center bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-blue-700 hover:border-blue-500 rounded-[10px]'>Submit</button>
        </form>
    </div>
  );
};

export default JobForm;
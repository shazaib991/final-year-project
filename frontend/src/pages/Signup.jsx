import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { Link, useNavigate } from 'react-router-dom';
import api from '../api';

const Signup = () => {
    const { register, handleSubmit, setError, formState: { errors } } = useForm();
    const navigate = useNavigate();
    const [isLoading, setIsLoading] = useState(false);

    const onSubmit = async (data) => {
        setIsLoading(true);
        try {
            await api.post('/auth/users/', data);
            // After signup, redirect to login
            navigate('/');
        } catch (error) {
            console.error(error);
            if (error.response && error.response.data) {
                // Handle specific field errors if possible
                Object.keys(error.response.data).forEach(key => {
                    setError(key, { type: 'manual', message: error.response.data[key] });
                });
            } else {
                setError('root', {
                    type: 'manual',
                    message: 'Registration failed. Try again.'
                });
            }
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center p-4">
            <div className="glass-panel p-8 w-full max-w-md animate-slide-up relative overflow-hidden">
                <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-green-400 to-primary-400"></div>
                <h2 className="text-3xl font-bold mb-6 text-center text-gray-800 tracking-tight">Create Account</h2>
                <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
                    <div className="space-y-1">
                        <label className="block text-sm font-medium text-gray-700 ml-1">Username</label>
                        <input
                            type="text"
                            {...register('username', { required: 'Username is required' })}
                            className="glass-input w-full"
                            placeholder="Choose a username"
                        />
                        {errors.username && <p className="text-red-500 text-sm ml-1">{errors.username.message}</p>}
                    </div>
                    <div className="space-y-1">
                        <label className="block text-sm font-medium text-gray-700 ml-1">Password</label>
                        <input
                            type="password"
                            {...register('password', { required: 'Password is required' })}
                            className="glass-input w-full"
                            placeholder="Choose a password"
                        />
                        {errors.password && <p className="text-red-500 text-sm ml-1">{errors.password.message}</p>}
                    </div>
                    {errors.root && <p className="text-red-500 text-sm text-center bg-red-50 p-2 rounded-lg border border-red-100">{errors.root.message}</p>}
                    <button
                        type="submit"
                        disabled={isLoading}
                        className="btn-primary w-full flex justify-center items-center gap-2 bg-green-600 hover:bg-green-700 shadow-green-600/30"
                    >
                        {isLoading ? (
                            <>
                                <svg className="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                </svg>
                                Creating Account...
                            </>
                        ) : 'Sign Up'}
                    </button>
                </form>
                <div className="mt-6 text-center">
                    <p className="text-sm text-gray-600">
                        Already have an account?{' '}
                        <Link to="/" className="font-medium text-primary-600 hover:text-primary-700 transition-colors">
                            Log in
                        </Link>
                    </p>
                </div>
            </div>
        </div>
    );
};

export default Signup;

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api';

const Dashboard = () => {
    const navigate = useNavigate();
    const [selectedFile, setSelectedFile] = useState(null);
    const [preview, setPreview] = useState(null);
    const [result, setResult] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleLogout = () => {
        localStorage.removeItem('auth_token');
        navigate('/');
    };

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setSelectedFile(file);
            setPreview(URL.createObjectURL(file));
            setResult(null);
            setError(null);
        }
    };

    const handlePredict = async () => {
        if (!selectedFile) return;

        setIsLoading(true);
        setError(null);

        const formData = new FormData();
        formData.append('image', selectedFile);

        try {
            const response = await api.post('/api/predict/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setResult(response.data);
        } catch (err) {
            setError('Failed to get prediction. Please try again.');
            console.error(err);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="min-h-screen pb-12">
            {/* Header */}
            <header className="sticky top-0 z-50 bg-white/70 backdrop-blur-lg border-b border-white/50 shadow-sm">
                <div className="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
                    <div className="flex items-center gap-3">
                        <div className="bg-primary-500 p-2 rounded-lg shadow-lg shadow-primary-500/30">
                            <svg className="w-6 h-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
                            </svg>
                        </div>
                        <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-primary-600 to-primary-800">
                            FractureDetector
                        </h1>
                    </div>
                    <button
                        onClick={handleLogout}
                        className="px-4 py-2 text-sm font-medium text-red-600 bg-red-50 hover:bg-red-100 rounded-lg transition-colors border border-red-100"
                    >
                        Sign Out
                    </button>
                </div>
            </header>

            <main className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
                <div className="glass-panel p-8 animate-fade-in">
                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
                        {/* Upload Section */}
                        <div className="animate-slide-up" style={{ animationDelay: '0.1s' }}>
                            <h2 className="text-xl font-semibold mb-6 flex items-center gap-2 text-gray-800">
                                <span className="bg-blue-100 text-blue-600 p-1.5 rounded-md">
                                    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
                                </span>
                                Upload X-Ray
                            </h2>

                            <div className="group relative">
                                <label
                                    htmlFor="file-upload"
                                    className={`relative flex flex-col items-center justify-center w-full h-80 rounded-2xl border-2 border-dashed transition-all duration-300 cursor-pointer overflow-hidden ${selectedFile
                                            ? 'border-primary-400 bg-primary-50'
                                            : 'border-gray-300 bg-gray-50/50 hover:bg-white hover:border-primary-400 hover:shadow-lg hover:shadow-primary-500/10'
                                        }`}
                                >
                                    {preview ? (
                                        <img src={preview} alt="Preview" className="w-full h-full object-contain p-4 transition-transform duration-500 group-hover:scale-105" />
                                    ) : (
                                        <div className="flex flex-col items-center justify-center pt-5 pb-6 text-center p-8">
                                            <div className="mb-4 text-gray-400 group-hover:text-primary-500 transition-colors duration-300">
                                                <svg className="w-16 h-16 mx-auto animate-bounce" style={{ animationDuration: '3s' }} fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
                                            </div>
                                            <p className="mb-2 text-lg font-medium text-gray-700">Click to upload or drag & drop</p>
                                            <p className="text-sm text-gray-500">Supports PNG, JPG, JPEG</p>
                                        </div>
                                    )}
                                    <input id="file-upload" name="file-upload" type="file" className="sr-only" onChange={handleFileChange} accept="image/*" />
                                </label>
                            </div>

                            <button
                                onClick={handlePredict}
                                disabled={!selectedFile || isLoading}
                                className={`mt-6 w-full btn-primary flex justify-center items-center gap-2 ${!selectedFile && 'opacity-50 cursor-not-allowed bg-gray-400 hover:bg-gray-400 shadow-none'
                                    }`}
                            >
                                {isLoading ? (
                                    <>
                                        <svg className="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                        </svg>
                                        Analyzing X-Ray...
                                    </>
                                ) : (
                                    <>
                                        <span>Analyze Image</span>
                                        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
                                    </>
                                )}
                            </button>
                            {error && <p className="text-red-500 text-sm mt-3 text-center bg-red-50 p-2 rounded-lg border border-red-100 animate-pulse">{error}</p>}
                        </div>

                        {/* Results Section */}
                        <div className="animate-slide-up flex flex-col" style={{ animationDelay: '0.2s' }}>
                            <h2 className="text-xl font-semibold mb-6 flex items-center gap-2 text-gray-800">
                                <span className="bg-purple-100 text-purple-600 p-1.5 rounded-md">
                                    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
                                </span>
                                Analysis Result
                            </h2>

                            <div className={`flex-grow rounded-2xl border-2 transition-all duration-500 flex flex-col items-center justify-center p-8 ${result
                                    ? 'bg-white border-transparent shadow-inner'
                                    : 'border-dashed border-gray-200 bg-gray-50/50'
                                }`}>
                                {result ? (
                                    <div className="text-center w-full animate-fade-in space-y-8">
                                        <div className="relative inline-block">
                                            <div className={`w-32 h-32 rounded-full flex items-center justify-center border-4 shadow-xl ${result.label === 'fractured'
                                                    ? 'bg-red-50 border-red-500 text-red-600'
                                                    : 'bg-green-50 border-green-500 text-green-600'
                                                }`}>
                                                {result.label === 'fractured' ? (
                                                    <svg className="w-16 h-16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>
                                                ) : (
                                                    <svg className="w-16 h-16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                                                )}
                                            </div>
                                            <div className={`absolute -bottom-2 -right-2 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider text-white shadow-lg ${result.label === 'fractured' ? 'bg-red-500' : 'bg-green-500'
                                                }`}>
                                                {result.label}
                                            </div>
                                        </div>

                                        <div className="space-y-4 max-w-xs mx-auto">
                                            <div>
                                                <div className="flex justify-between text-sm font-medium mb-1">
                                                    <span className="text-gray-600">Confidence Score</span>
                                                    <span className="text-gray-900">{(result.confidence * 100).toFixed(1)}%</span>
                                                </div>
                                                <div className="w-full bg-gray-200 rounded-full h-2.5 overflow-hidden">
                                                    <div
                                                        className={`h-2.5 rounded-full transition-all duration-1000 ease-out ${result.label === 'fractured' ? 'bg-red-500' : 'bg-green-500'
                                                            }`}
                                                        style={{ width: `${result.confidence * 100}%` }}
                                                    ></div>
                                                </div>
                                                <p className="text-xs text-gray-400 mt-2">
                                                    Raw Prediction Value: {result.raw_prediction.toFixed(4)}
                                                </p>
                                            </div>
                                        </div>
                                    </div>
                                ) : (
                                    <div className="text-gray-400 text-center">
                                        <div className="bg-gray-100 p-4 rounded-full inline-block mb-4">
                                            <svg className="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                                        </div>
                                        <p className="font-medium">No Image Analyzed</p>
                                        <p className="text-sm mt-1">Upload an image and click "Analyze" to see results</p>
                                    </div>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    );
};

export default Dashboard;

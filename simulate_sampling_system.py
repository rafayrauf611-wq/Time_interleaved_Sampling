import numpy as np
import matplotlib.pyplot as plt

def simulate_sampling_system():
    """
    Simulates a time-interleaved sampling system with impulse at a 10Hz sampling instant.
    """
    
    # ---------------------------------------------------------
    # 1. SETUP PARAMETERS
    # ---------------------------------------------------------
    # Choose a time that IS a 10Hz sampling instant
    # 10Hz sampling: 0, 0.1, 0.2, ... 5.9, 6.0, etc.
    # Let's choose 5.90 seconds (which would be ID "123" for example)
    target_time = 1.23
    
    print(f"Target Impulse Location: {target_time:.2f} seconds")
    print(f"Note: This IS a 10Hz sampling instant (multiple of 0.1)")

    # Simulation Resolution (1000 Hz to represent continuous time)
    fs_sim = 1000 
    duration = 10 # seconds
    t_cont = np.linspace(0, duration, duration * fs_sim + 1)
    
    # ---------------------------------------------------------
    # 2. GENERATE CONTINUOUS SIGNAL
    # ---------------------------------------------------------
    x_cont = np.zeros_like(t_cont)
    
    # Find index closest to target time and place impulse
    target_idx = np.argmin(np.abs(t_cont - target_time))
    x_cont[target_idx] = 1.0 
    
    # ---------------------------------------------------------
    # 3. SINGLE 10 HZ SAMPLER (Standard)
    # ---------------------------------------------------------
    t_10hz = t_cont[::100]
    x_10hz = x_cont[::100]
    
    # Check if detection failed
    if np.sum(x_10hz) == 0:
        print("Standard 10Hz Sampler Result: FAILED (Signal missed)")
        status_std = "FAILED (Signal Missed)"
    else:
        print("Standard 10Hz Sampler Result: SUCCESS (Signal detected)")
        status_std = "SUCCESS (Signal Detected)"
        # Find which sample captured it
        detected_sample_idx = np.argmax(x_10hz)
        detected_sample_time = t_10hz[detected_sample_idx]
        print(f"  Impulse captured at sample #{detected_sample_idx}, time={detected_sample_time:.2f}s")

    # ---------------------------------------------------------
    # 4. DESIGNED SYSTEM (10 Parallel Branches)
    # ---------------------------------------------------------
    fs_final = 100
    num_samples_final = duration * fs_final + 1
    x_final_100hz = np.zeros(num_samples_final)
    t_final_100hz = np.linspace(0, duration, num_samples_final)
    
    print("\nSimulating 10 Parallel Branches...")
    
    for k in range(10):
        # Branch k captures offset k/100 sec
        offset_samples = k * 10 
        branch_output = x_cont[offset_samples::100]
        
        # Add to final array (Interleaving)
        limit = min(len(branch_output), len(x_final_100hz[k::10]))
        x_final_100hz[k::10][:limit] = branch_output[:limit]

    # Check verification
    if np.sum(x_final_100hz) > 0:
        detected_time = t_final_100hz[np.argmax(x_final_100hz)]
        print(f"Designed System Result: SUCCESS. Detected at t={detected_time:.2f}s")
    else:
        print("Designed System Result: FAILED.")

    # ---------------------------------------------------------
    # 5. PLOTTING
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 10))
    
    # Plot 1: Continuous
    plt.subplot(3, 1, 1)
    plt.plot(t_cont, x_cont, 'b')
    plt.axvline(x=target_time, color='r', linestyle='--', alpha=0.5, label=f'Impulse at {target_time}s')
    plt.title(f'1. Continuous Input (Impulse at {target_time:.2f}s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    
    # Plot 2: Standard 10Hz
    plt.subplot(3, 1, 2)
    plt.stem(t_10hz, x_10hz, linefmt='r-', markerfmt='ro', basefmt='k')
    
    # Highlight the successful sample
    if np.sum(x_10hz) > 0:
        success_idx = np.argmax(x_10hz)
        plt.plot(t_10hz[success_idx], x_10hz[success_idx], 'go', markersize=12, 
                markeredgecolor='k', markeredgewidth=2, label='Successful Detection')
        plt.legend()
    
    plt.title(f'2. Standard 10Hz Sampler: {status_std}')
    plt.ylabel('Amplitude')
    plt.grid(True)
    
    # Plot 3: Final System Output
    plt.subplot(3, 1, 3)
    plt.stem(t_final_100hz, x_final_100hz, linefmt='g-', markerfmt='go', basefmt='k')
    plt.title('3. Final Output of Designed System (Resampled at 100Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# ==========================================
# RUN SIMULATION WITH IMPULSE AT 10Hz SAMPLING INSTANT
# ==========================================
simulate_sampling_system()

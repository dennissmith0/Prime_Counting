use std::collections::HashSet;
use std::sync::Arc;
use std::thread;

fn main() {
    let x = create_and_count(1_000_000);
    println!("The result is: {x}");
}

fn create_and_count(n: i32) -> u64 {
    let deltas: [i8; 2] = [-1, 1];
    let mut count = 0;
    let mut poss = vec![];
    for val in (6..n + 1).step_by(6) {
        for &delta in &deltas {
            poss.push((count, val + i32::from(delta)));
            count += 1;
        }
    }
    let poss = Arc::new(poss);

    let mut mult: HashSet<i32> = HashSet::new();

    let threads = num_cpus::get(); // Get the number of CPUs
    let mut handles = vec![];

    for i in 0..threads {
        let poss = Arc::clone(&poss);
        let handle = thread::spawn(move || {
            let slice = (poss.len() * i / threads)..(poss.len() * (i + 1) / threads);
            let local_poss = &poss[slice];
            let mut local_mult = HashSet::new();
            for &(idx, i) in local_poss {
                for &(_, j) in &poss[idx..] {
                    if let Some(product) = i.checked_mul(j) {
                        if product <= n {
                            local_mult.insert(product);
                        }
                    }
                }
            }
            local_mult
        });
        handles.push(handle);
    }

    for handle in handles {
        let hs = handle.join().unwrap();
        mult.extend(&hs);
    }

    (poss.len() - mult.len() + 2) as u64
}

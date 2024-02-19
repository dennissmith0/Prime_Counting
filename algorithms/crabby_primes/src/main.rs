// use std::collections::HashSet;

// use std::thread::spawn;

// fn main() {
//     let x = create_and_count(1_000_000);
//     println!("The result is: {x}");
// }

// fn create_and_count(n: i32) -> u64 {
//     let deltas: [i8; 2] = [-1, 1];
//     let mut count = 0;
//     let mut poss = vec![];
//     for val in (6..n + 1).step_by(6) {
//         for delta in deltas {
//             poss.push((count, val + delta as i32));
//             count += 1;
//         }
//     }
//     // println!("{poss:?}");

//     // let poss = (6..n + 1)
//     //     .step_by(6)
//     //     .flat_map(|i| deltas.iter().map(move |d| *d as i128 + i))
//     //     .collect::<Vec<_>>();

//     // let mut mult = HashSet::new();
//     let mult = poss
//         .par_iter()
//         .flat_map(|(idx, i)| {
//             poss[*idx..]
//                 .par_iter()
//                 .filter_map(move |(_, j)| if i * j <= n { Some(*i * *j) } else { None })
//         })
//         .collect::<HashSet<i32>>();
//     // for (idx, i) in poss.iter().enumerate() {
//     //     for j in &poss[idx..] {
//     //         let product = i * j;
//     //         if product > n {
//     //             break;
//     //         }
//     //         mult.insert(product);
//     //     }
//     // }
//     // println!("{mult:?}");

//     (poss.len() - mult.len() + 2) as u64
// }
use num_cpus;
use std::collections::HashSet;
use std::sync::{Arc, Mutex};
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
    let mult = Arc::new(Mutex::new(HashSet::new()));

    let threads = num_cpus::get(); // Get the number of CPUs
    let mut handles = vec![];

    for i in 0..threads {
        let poss = Arc::clone(&poss);
        let mult = Arc::clone(&mult);
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
            let mut mult = mult.lock().unwrap();
            *mult = mult.union(&local_mult).cloned().collect();
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    let mult = mult.lock().unwrap();
    (poss.len() - mult.len() + 2) as u64
}
